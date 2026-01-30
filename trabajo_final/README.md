# Trabajo Final: Análisis de Desarrollo Global

Este proyecto integrador pone a prueba todas las habilidades adquiridas durante el curso. Actuarás como un **Data Scientist Senior** contratado por un organismo internacional (ONU/Banco Mundial) para analizar patrones de desarrollo global.

---

## 🎯 Objetivo General

Construir un **pipeline de análisis de datos reproducible** que, partiendo de datos crudos (Quality of Government Dataset), limpie, transforme, analice y visualice clusters de países según su desempeño institucional y económico.

---

## 🛠️ Requisitos Técnicos

El proyecto debe implementarse en **Python** y cumplir con:

### 1. Ingeniería de Datos (ETL)
- **Ingesta:** Descarga automática o validación del dataset QoG (`qog_std_ts`).
- **Limpieza:** Manejo de nulos, estandarización de columnas, conversión de tipos.
- **Tecnología:** Debes usar **Dask** o **PySpark** para demostrar escalabilidad (aunque el dataset quepa en RAM, simula que es Big Data).

### 2. Análisis Exploratorio (EDA)
- Estadísticas descriptivas de variables clave (Democracia, Corrupción, PIB).
- Análisis de correlaciones.
- Detección de outliers.

### 3. Machine Learning (Clustering)
- Implementa un algoritmo de **Clustering (K-Means o Jerárquico)** para agrupar países similares.
- **Variables sugeridas:** `pib_per_capita`, `indice_corrupcion`, `esperanza_vida`, `estabilidad_politica`.
- Determina el número óptimo de clusters (Método del Codo o Silhouette).

### 4. Visualización y Reporte
- Genera al menos 3 visualizaciones clave (scatterplot de clusters, mapa coroplético, evolución temporal).
- Interpretación de los clusters: ¿Qué caracteriza al "Cluster 1"? ¿Y al "Cluster 2"?

---

## 📂 Entregables

Debes subir a `entregas/trabajo_final/TU_USUARIO/`:

1. **`main.py`:** Script principal que orquesta todo el proceso.
2. **`etl.py`:** Módulo de limpieza y preparación.
3. **`analisis.py`:** Módulo de ML y visualización.
4. **`INFORME.md`:** Un reporte ejecutivo breve explicando tus hallazgos (con las gráficas generadas).
5. **`requirements.txt`:** Librerías necesarias.

---

## ⚖️ Rúbrica de Evaluación

| Criterio | Peso | Descripción |
|----------|------|-------------|
| **Código Limpio** | 20% | Estructura modular, PEP8, comentarios claros. |
| **Uso de Big Data** | 20% | Correcta implementación de Dask/Spark (lazy evaluation). |
| **Rigor Analítico** | 30% | Correcta aplicación de ML, validación de clusters, manejo estadísticas. |
| **Reproducibilidad**| 15% | ¿El código corre en otra máquina sin errores? |
| **Informe** | 15% | Claridad en la comunicación de hallazgos. |

---

## 📅 Fecha Límite

Consultar con el instructor o plataforma del curso.

¡Éxito! 🚀
