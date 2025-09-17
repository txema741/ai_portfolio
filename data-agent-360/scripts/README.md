# ⚙️ Scripts – Data Agent 360

En esta carpeta se recopilan los **scripts en Python** que componen la lógica del proyecto.  
Cada script está diseñado para ejecutar una tarea concreta de auditoría, limpieza o análisis de datos empresariales.

---

## 📂 Scripts disponibles

### 🐍 `audit_clientes.py`
- **Descripción:**  
  Auditoría de un dataset de clientes en formato Excel.  
  Incluye:
  - Perfil de calidad de los datos (filas, nulos, duplicados exactos y de negocio).  
  - Detección de ventas negativas y a cero.  
  - Identificación de outliers mediante IQR.  
  - Recomendaciones de negocio automáticas.  
  - Generación opcional de informe en Markdown en `/results/`.

- **Uso en Windows:**  
  ```powershell
  python scripts\audit_clientes.py data_sample\clientes.xlsx --reporte results\01_auditoria_clientes_result.md

Dependencias:
pip install pandas openpyxl tabulate
