# Ejercicio 1.1: Introducción a SQLite - Estructura del Directorio

Este documento sirve como índice para organizar y entender el propósito de cada archivo dentro de este ejercicio.

---

## 📂 Estructura de Archivos

Los archivos están agrupados por la fase del ejercicio a la que pertenecen.

### FASE 0: Análisis Exploratorio de Datos (EDA)
*   `eda_exploratorio.py`: Script principal que realiza un análisis automático de todos los archivos CSV.
*   `resumen_eda.txt`: Salida en texto plano generada por el script `eda_exploratorio.py`.
*   `resumen_eda.md`: Versión en Markdown del resumen del EDA para mejor visualización.
*   `ANALISIS_DATOS.md`: Documento manual con los hallazgos, conclusiones y diagramas Entidad-Relación (ER) basados en el EDA.

### FASE 1-3: Creación de Modelos de Base de Datos
*   `solucion_modelo_a.py`: Script que genera la base de datos `tienda_modelo_a.db` (Modelo Desnormalizado).
*   `solucion_modelo_b.py`: Script que genera la base de datos `tienda_modelo_b.db` (Modelo Normalizado).
*   `solucion_modelo_c.py`: Script que genera la base de datos `tienda_modelo_c.db` (Modelo E-commerce Completo).

### FASE 4: Verificación y Consultas
*   `consultas_verificacion.sql`: Contiene ejemplos de consultas SQL para probar y verificar los datos en cada uno de los tres modelos.
*   `consultas_comparativas.py`: Script de Python que ejecuta consultas en los diferentes modelos y muestra los resultados, permitiendo comparar su rendimiento y complejidad.

### FASE 5: Documentación y Reflexión
*   `REFLEXION.md`: Documento con las respuestas a las preguntas sobre las ventajas y desventajas de cada modelo de datos.
*   `TEORIA.md`: Apuntes teóricos sobre SQLite y conceptos de bases de datos relevantes para el ejercicio.
*   `README.md`: Este mismo archivo, que sirve como guía del directorio.

### Extras: Dashboards y Visualización
*   `dashboard.py`: Aplicación interactiva (Streamlit) para visualizar los datos del Modelo B.
*   `dashboard_modelo_a.py`: Aplicación interactiva (Streamlit) para visualizar los datos del Modelo A.

### Scripts Auxiliares (Borradores o Helpers)
*   `crear_bases_datos.py`: Script borrador o de ayuda para la creación de las bases de datos.
*   `verificar_bases_datos.py`: Script borrador o de ayuda para la verificación de datos.

---
**Nota:** Los archivos de base de datos (`.db`) son generados por los scripts `solucion_*.py` y no deben ser subidos al repositorio, ya que están incluidos en `.gitignore`.
