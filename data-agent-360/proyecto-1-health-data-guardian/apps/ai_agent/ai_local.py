# -*- coding: utf-8 -*-
"""
Health Data Guardian – V4 (Local, sin API de pago)
Agente conversacional local que responde preguntas sobre los resultados de auditoría.
- Usa sentence-transformers para embeddings (all-MiniLM-L6-v2)
- Usa FAISS para búsqueda por similitud
- Usa Flan-T5-small (transformers) para generar respuestas naturales a partir de documentos recuperados
Todo es gratuito; los modelos se descargan desde Hugging Face la primera vez.
"""

from pathlib import Path
import streamlit as st
import pandas as pd
import json
import os
from typing import List
import faiss
import numpy as np

# Embeddings
from sentence_transformers import SentenceTransformer

# Generación (gratuito - Hugging Face)
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# --- CONFIG ---
ROOT = Path(__file__).resolve().parents[2]  # proyecto root
RESULTS = ROOT / "results"

EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # rápido y ligero
GEN_MODEL_NAME = "google/flan-t5-small"  # pequeño y libre (se descarga la primera vez)
EMBED_DIM = 384  # dim de all-MiniLM-L6-v2

# Tamaño de chunk y overlap para dividir documentos
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# --- UTILIDADES ---
def load_corpus() -> List[str]:
    """Carga textos concatenados de results/ (issues, profile, analyst_summary)."""
    parts = []
    issues_file = RESULTS / "issues_detectados.csv"
    if issues_file.exists():
        try:
            df = pd.read_csv(issues_file)
            parts.append("Issues Detectados:\n" + df.to_string(index=False))
        except Exception:
            parts.append("Issues Detectados: (error leyendo CSV)")
    profile_file = RESULTS / "profile.json"
    if profile_file.exists():
        parts.append("Profile:\n" + profile_file.read_text(encoding="utf-8"))
    summary_file = RESULTS / "analyst_summary.md"
    if summary_file.exists():
        parts.append("Analyst Summary:\n" + summary_file.read_text(encoding="utf-8"))
    return parts

def chunk_text(text: str, size: int=CHUNK_SIZE, overlap: int=CHUNK_OVERLAP) -> List[str]:
    """Divide texto en chunks solapados simples."""
    tokens = text.split()
    chunks = []
    i = 0
    while i < len(tokens):
        chunk = tokens[i:i+size]
        chunks.append(" ".join(chunk))
        i += size - overlap
    return chunks

def build_corpus_chunks() -> List[str]:
    parts = load_corpus()
    all_chunks = []
    for p in parts:
        all_chunks.extend(chunk_text(p))
    # Filtrar chunks muy pequeños
    return [c for c in all_chunks if len(c.strip())>20]

# --- INDEX / EMBEDDINGS ---
@st.cache_resource
def get_embedding_model():
    return SentenceTransformer(EMBED_MODEL_NAME)

@st.cache_resource
def build_faiss_index(chunks: List[str]):
    model = get_embedding_model()
    embeddings = model.encode(chunks, convert_to_numpy=True, show_progress_bar=False)
    index = faiss.IndexFlatIP(EMBED_DIM)  # inner product (cos sim after normalize)
    # normalizar para usar IP como cos sim
    faiss.normalize_L2(embeddings)
    index.add(embeddings)
    return index, embeddings

# --- GENERATOR (Flan-T5) ---
@st.cache_resource
def get_generator():
    # Cargar tokenizer y modelo; la primera vez hará download (gratuito)
    tokenizer = AutoTokenizer.from_pretrained(GEN_MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(GEN_MODEL_NAME)
    gen = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)
    return gen

def retrieve_relevant_chunks(query: str, chunks: List[str], index, embeddings, top_k: int=4):
    model = get_embedding_model()
    q_emb = model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(q_emb)
    D, I = index.search(q_emb, top_k)
    results = []
    for idx in I[0]:
        if idx < len(chunks):
            results.append(chunks[idx])
    return results

def make_prompt(query: str, retrieved: List[str]) -> str:
    """Construye prompt conciso para el generador."""
    context = "\n\n---\n\n".join(retrieved)
    prompt = (
        "Eres un asistente que responde preguntas sobre la calidad de datos clínicos.\n"
        "Usa únicamente la información del contexto siguiente. Si no hay respuesta, dilo claramente.\n\n"
        "Contexto:\n" + context + "\n\n"
        "Pregunta: " + query + "\n\n"
        "Respuesta (concisa, en español):"
    )
    # Truncar por seguridad si muy largo
    return prompt[:4000]

# --- STREAMLIT UI ---
st.set_page_config(page_title="Health Data Guardian – Agente Local (V4)", layout="wide")
st.title("🤖 Agente local: preguntas sobre auditoría (V4) — sin APIs de pago")
st.caption("Carga V1/V2/V3 primero para tener datos en carpeta `results/`.")

st.markdown(
    "Este agente funciona **localmente**: usa sentence-transformers + FAISS para recuperar "
    "fragmentos y Flan-T5-small para generar respuestas. La primera ejecución descargará modelos."
)

# Cargar corpus y construir index
chunks = build_corpus_chunks()
if not chunks:
    st.error("No se encontraron documentos en results/. Ejecuta V1-V3 primero para generar issues/profile/analyst_summary.")
    st.stop()

with st.spinner("Cargando modelos y construyendo índice (puede tardar la primera vez)..."):
    index, embeddings = build_faiss_index(chunks)
    gen = get_generator()

# Chat
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Pregunta (ej.: ¿qué campo tiene más errores de formato?)")
if st.button("Enviar") and user_input:
    retrieved = retrieve_relevant_chunks(user_input, chunks, index, embeddings, top_k=5)
    # Si no hay relevante, devolvemos extractivo simple
    if not retrieved:
        st.write("No he encontrado información relevante en los resultados.")
    else:
        prompt = make_prompt(user_input, retrieved)
        try:
            out = gen(prompt, max_length=256, do_sample=False)[0]["generated_text"]
            answer = out.strip()
        except Exception as e:
            # Fallback: devolver los fragmentos recuperados si la generación falla
            answer = "No se pudo generar respuesta. Fragmentos relevantes:\n\n" + "\n\n---\n\n".join(retrieved)
        st.session_state.history.append((user_input, answer))

# Mostrar chat
for q, a in reversed(st.session_state.history[-10:]):
    st.markdown(f"**Tú:** {q}")
    st.markdown(f"**Agente:** {a}")
