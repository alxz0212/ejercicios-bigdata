# Big Data con Python - De Cero a Producción

<div align="center">

<img src="docs/assets/todoeconometria_logo.png" alt="TodoEconometria" width="350">

*"Sin experiencia no hay conocimiento"*

## CURSO COMPLETO DE BIG DATA

[![GitHub Stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=for-the-badge&logo=github)](https://github.com/TodoEconometria/ejercicios-bigdata/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/TodoEconometria/ejercicios-bigdata?style=for-the-badge&logo=github)](https://github.com/TodoEconometria/ejercicios-bigdata/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Deploy](https://github.com/TodoEconometria/ejercicios-bigdata/actions/workflows/docs.yml/badge.svg)](https://github.com/TodoEconometria/ejercicios-bigdata/actions/workflows/docs.yml)

### [**Ver Sitio Web del Curso**](https://todoeconometria.github.io/ejercicios-bigdata/)

<<<<<<< HEAD
### Paso 1: Haz un Fork de este Repositorio

Un **fork** es tu copia personal de este proyecto donde trabajarás sin afectar el original.

1. Haz clic en el botón **Fork** (arriba a la derecha en GitHub)
2. Selecciona tu cuenta personal
3. ¡Listo! Ahora tienes tu propia copia

### Paso 2: Configura tu Proyecto

**IMPORTANTE**: Sigue las instrucciones completas en:
### 👉 **[INSTRUCCIONES_CONFIGURACION.md](./INSTRUCCIONES_CONFIGURACION.md)** 👈

Este archivo te guiará paso a paso para:
- Clonar el repositorio
- Crear las carpetas de trabajo
- Copiar las plantillas de ejercicios
- Instalar Python y dependencias
- Descargar los datos

### Paso 3: Lee las Guías

Este repositorio incluye guías para ayudarte:

- **[INSTRUCCIONES_CONFIGURACION.md](./INSTRUCCIONES_CONFIGURACION.md)**: Configuración inicial (¡empieza aquí!)
- **[GUIA_GIT_GITHUB.md](./GUIA_GIT_GITHUB.md)**: Todo sobre Git y GitHub
- **[GUIA_IA_ASISTENTE.md](./GUIA_IA_ASISTENTE.md)**: Cómo usar IA para aprender (Gemini, Claude, ChatGPT)
- **[LEEME.md](./LEEME.md)**: Instrucciones técnicas de los ejercicios
- **[ARQUITECTURA_Y_STACK.md](./ARQUITECTURA_Y_STACK.md)**: Conceptos avanzados (opcional)

### Paso 4: Prepara tu Entorno

Necesitarás:
- **Python 3.8+** instalado ([Descargar aquí](https://www.python.org/downloads/))
- **Git** instalado ([Descargar aquí](https://git-scm.com/downloads))
- Un editor de código (recomendamos [VS Code](https://code.visualstudio.com/) o PyCharm)

## Estructura del Proyecto

```
ejercicios_bigdata/
├── README.md                       # Este archivo
├── INSTRUCCIONES_CONFIGURACION.md  # Configuración inicial (¡LEE ESTO PRIMERO!)
├── GUIA_GIT_GITHUB.md              # Guía de Git para principiantes
├── GUIA_IA_ASISTENTE.md            # Guía para usar IA (Gemini, Claude, ChatGPT)
├── LEEME.md                        # Instrucciones técnicas de ejercicios
├── ARQUITECTURA_Y_STACK.md         # Conceptos técnicos
├── requirements.txt                # Librerías Python necesarias
├── PROGRESO.md                     # Tu checklist de avance
├── plantillas/                     # Plantillas originales (NO modificar)
│   ├── datos/
│   │   └── descargar_datos.py      # Plantilla del script de descarga
│   └── ejercicios/
│       ├── 01_cargar_sqlite.py     # Plantilla ejercicio 1
│       ├── 02_limpieza_datos.py    # Plantilla ejercicio 2
│       ├── 03_parquet_dask.py      # Plantilla ejercicio 3
│       └── 04_pyspark_query.py     # Plantilla ejercicio 4
├── datos/                          # TU carpeta (crearás después)
│   └── descargar_datos.py          # Tu copia para trabajar
└── ejercicios/                     # TU carpeta (crearás después)
    ├── 01_cargar_sqlite.py         # Tu ejercicio 1
    ├── 02_limpieza_datos.py        # Tu ejercicio 2
    ├── 03_parquet_dask.py          # Tu ejercicio 3
    └── 04_pyspark_query.py         # Tu ejercicio 4
```

**Nota**: Las carpetas `datos/` y `ejercicios/` NO están en el repositorio inicial. Las crearás siguiendo **[INSTRUCCIONES_CONFIGURACION.md](./INSTRUCCIONES_CONFIGURACION.md)**.

## Cómo Trabajar en este Proyecto

### Sigue este Orden:

1. **Lee** → [INSTRUCCIONES_CONFIGURACION.md](./INSTRUCCIONES_CONFIGURACION.md) (configuración completa)
2. **Lee** → [GUIA_GIT_GITHUB.md](./GUIA_GIT_GITHUB.md) (si no conoces Git)
3. **Lee** → [GUIA_IA_ASISTENTE.md](./GUIA_IA_ASISTENTE.md) (cómo usar Gemini y otras IAs)
4. **Lee** → [LEEME.md](./LEEME.md) (instrucciones de ejercicios)
5. **Comienza** → Ejercicio 01_cargar_sqlite.py
6. **Actualiza** → PROGRESO.md después de cada ejercicio
7. **Haz commit y push** → Sube tu progreso a GitHub regularmente

## Seguimiento de tu Progreso

1. Abre el archivo [PROGRESO.md](./PROGRESO.md)
2. Marca ✅ cada ejercicio que completes
3. Haz commit de tus cambios regularmente
4. Sube (push) tus commits a GitHub

Tu profesor podrá ver tu progreso en tu fork.

## Cómo Pedir Ayuda

### Opción 1: Usa IA como Asistente
Lee la [GUIA_IA_ASISTENTE.md](./GUIA_IA_ASISTENTE.md) para aprender a pedir ayuda a herramientas como:
- Claude Code
- GitHub Copilot
- ChatGPT

### Opción 2: Abre un Issue
Si tienes problemas:
1. Ve a la pestaña "Issues" en tu fork
2. Crea un nuevo issue describiendo el problema
3. Comparte el enlace con tu profesor

### Opción 3: Pregunta a tu Profesor
Comparte el enlace de tu fork con tu profesor para que vea tu código.

## Reglas de Oro

1. **No tengas miedo de equivocarte**: Los errores son parte del aprendizaje
2. **Haz commits frecuentes**: Guarda tu progreso regularmente
3. **Lee los comentarios del código**: Ahí está la explicación
4. **Usa la IA con criterio**: Úsala para entender, no solo para copiar
5. **Pide ayuda cuando la necesites**: Nadie nace sabiendo

## Recursos Adicionales

- [Documentación oficial de Python](https://docs.python.org/es/)
- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Tutorial interactivo de Git](https://learngitbranching.js.org/?locale=es_ES)
- [Curso gratuito de Big Data (YouTube)](https://www.youtube.com/results?search_query=big+data+python+tutorial+español)

## Licencia

Este material es de uso educativo. Siéntete libre de aprender y compartir.
=======
</div>
>>>>>>> upstream/main

---

## Demos en Vivo

| Observatorio Sísmico Global | ISS Tracker |
|:---------------------------:|:-----------:|
| Sismos en tiempo real desde USGS API | Rastrea la Estación Espacial Internacional |
| [**Ver Demo**](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/dashboard_sismos_global.html) | [**Ver Demo**](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/dashboard_iss_tracker.html) |

*Dashboards con datos reales de APIs públicas, actualizados automáticamente*

---

## El Curso en Números

| 230 Horas | 9 Módulos | 25+ Ejercicios | 12+ Dashboards | 30+ Tecnologías |
|:---------:|:---------:|:--------------:|:--------------:|:---------------:|
| de contenido | completos | prácticos | interactivos | profesionales |

---

## Stack Tecnológico Completo

### Bases de Datos

| Tecnología | Nivel | Qué Aprenderás |
|------------|-------|----------------|
| **SQLite** | Básico | Queries SQL, índices, optimización |
| **PostgreSQL** | Intermedio | Joins complejos, Window Functions, CTEs |
| **Oracle** | Avanzado | PL/SQL, procedimientos almacenados |
| **DynamoDB** | Avanzado | NoSQL, key-value, serverless |

### Procesamiento de Datos

| Tecnología | Cuándo Usarla | Escala |
|------------|---------------|--------|
| **Pandas** | Análisis exploratorio | < 5 GB |
| **Dask** | Datasets grandes, 1 máquina | 5-100 GB |
| **Apache Spark** | Clusters, producción | > 100 GB |
| **Spark Streaming** | Datos en tiempo real | Ilimitado |

### Streaming y Cloud

| Tecnología | Propósito |
|------------|-----------|
| **Apache Kafka** | Streaming distribuido (KRaft mode) |
| **Spark Structured Streaming** | Procesamiento de streams |
| **LocalStack** | Simulación AWS local (gratis) |
| **Terraform** | Infraestructura como Código |
| **AWS S3/Lambda** | Almacenamiento y funciones serverless |

### Machine Learning e IA

| Tecnología | Aplicación |
|------------|------------|
| **Scikit-learn** | ML clásico, clustering, clasificación |
| **TensorFlow** | Deep Learning, redes neuronales |
| **MobileNetV2** | Transfer Learning, Computer Vision |
| **ARIMA/SARIMA** | Series temporales, forecasting |

### NLP y Visualización

| Tecnología | Uso |
|------------|-----|
| **NLTK** | Procesamiento de lenguaje natural |
| **TF-IDF** | Vectorización de texto |
| **Plotly** | Dashboards interactivos |
| **Leaflet.js** | Mapas interactivos |

### Econometría

| Tecnología | Aplicación |
|------------|------------|
| **linearmodels** | Datos de panel |
| **Panel OLS** | Efectos fijos y aleatorios |
| **Hausman Test** | Selección de modelo |

---

## Módulos del Curso

### Módulo 1: Bases de Datos
> SQLite, PostgreSQL, Oracle, migraciones

Desde tu primera query SELECT hasta procedimientos almacenados en Oracle.

### Módulo 2: Limpieza de Datos y ETL
> Pipeline ETL profesional, QoG Dataset (1289 variables, 194+ países)

Pipelines profesionales que procesan millones de registros.

### Módulo 3: Procesamiento Distribuido
> Dask, Parquet, LocalCluster

Procesamiento paralelo de datasets grandes en una sola máquina.

### Módulo 4: Machine Learning
> PCA, K-Means, Transfer Learning, ARIMA/SARIMA

Desde clustering hasta Computer Vision con TensorFlow y series temporales.

### Módulo 5: NLP y Text Mining
> NLTK, TF-IDF, Jaccard, Análisis de Sentimiento

Tokenización, limpieza, similitud de documentos y análisis de sentimiento.

### Módulo 6: Análisis de Datos de Panel
> Efectos Fijos, Efectos Aleatorios, Hausman Test

Análisis longitudinal con datos país x año.

### Módulo 7: Infraestructura Big Data
> Docker, Docker Compose, Apache Spark Cluster

Contenedores, orquestación y clusters Spark en Docker.

### Módulo 8: Streaming con Kafka
> Apache Kafka (KRaft), Spark Structured Streaming

Streaming en tiempo real con datos de sismos desde USGS API.

### Módulo 9: Cloud con LocalStack
> LocalStack, Terraform, AWS S3/Lambda/DynamoDB

Simulación de AWS sin costos e Infraestructura como Código.

### Trabajo Final
> Docker + Spark + PostgreSQL + Análisis Completo

Proyecto integrador de principio a fin.

---

## Inicio Rápido

```bash
# 1. Clona tu fork
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata

# 2. Crea entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# 3. Instala dependencias
pip install -r requirements.txt
```

**Siguiente paso:** [Ver documentación completa](https://todoeconometria.github.io/ejercicios-bigdata/)

---

## Estructura del Repositorio

```
ejercicios-bigdata/
├── ejercicios/                 # Código por módulo
│   ├── 01_bases_de_datos/
│   ├── 02_limpieza_datos/
│   ├── 03_procesamiento_distribuido/
│   ├── 04_machine_learning/
│   ├── 05_nlp_text_mining/
│   ├── 06_analisis_datos_de_panel/
│   ├── 07_infraestructura_bigdata/
│   ├── 08_streaming_kafka/
│   └── 09_cloud_localstack/
│
├── entregas/                   # Zona de entregas del alumno
├── trabajo_final/              # Proyecto integrador
└── docs/                       # Sitio web (MkDocs)
```

---

## Galería de Dashboards

| Dashboard | Tecnologías |
|-----------|-------------|
| [**ARIMA PRO**](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/dashboard_arima_pro.html) | Series temporales estilo Bloomberg |
| [**PCA + K-Means**](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/02_pca_iris_dashboard.html) | Clustering y reducción dimensional |
| [**Transfer Learning Flores**](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/dashboard_flores.html) | CNN + Computer Vision |
| [**Panel Data QoG**](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/06_analisis_panel_qog.html) | Spark + PostgreSQL + ML |
| [**Sismos Global**](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/dashboard_sismos_global.html) | Kafka + Tiempo Real |
| [**ISS Tracker**](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/dashboard_iss_tracker.html) | LocalStack + AWS |

---

## Instructor

**Juan Marcelo Gutierrez Miranda** — [@TodoEconometria](https://www.linkedin.com/in/juangutierrezconsultor/)

10+ años en análisis de datos y Big Data. Formador de profesionales en toda Latinoamérica y España.

**Contacto:**
- Email: cursos@todoeconometria.com
- LinkedIn: [Juan Gutierrez](https://www.linkedin.com/in/juangutierrezconsultor/)
- Web: [todoeconometria.com](https://www.todoeconometria.com)

---

## Referencias Académicas

1. **Dean, J., & Ghemawat, S. (2008).** MapReduce: Simplified data processing on large clusters. *Communications of the ACM*.
2. **Zaharia, M., et al. (2016).** Apache Spark: A unified engine for big data processing. *Communications of the ACM*.
3. **McKinney, W. (2022).** *Python for Data Analysis*. O'Reilly Media.
4. **Kleppmann, M. (2017).** *Designing Data-Intensive Applications*. O'Reilly Media.

---

---

## English

> **This course is available in English!** Visit the [English version of the website](https://todoeconometria.github.io/ejercicios-bigdata/en/).

A **complete, free, open-source** Big Data course covering 230 hours of hands-on content across 9 modules:

- **Databases:** SQLite, PostgreSQL, Oracle, DynamoDB
- **ETL & Processing:** Pandas, Dask, Apache Spark
- **Streaming:** Apache Kafka (KRaft mode), Spark Structured Streaming
- **Cloud:** LocalStack (free AWS simulation), Terraform, Lambda
- **ML & AI:** PCA, K-Means, TensorFlow, ARIMA/SARIMA, Transfer Learning
- **NLP:** NLTK, TF-IDF, Sentiment Analysis, Jaccard Similarity
- **Econometrics:** Panel Data, Fixed/Random Effects, Hausman Test
- **Infrastructure:** Docker, Docker Compose, Spark Clusters

**Live demos:** [Global Earthquake Observatory](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/dashboard_sismos_global.html) | [ISS Tracker](https://todoeconometria.github.io/ejercicios-bigdata/dashboards/dashboard_iss_tracker.html)

---

<div align="center">

**© 2026 Juan Marcelo Gutierrez Miranda** — Open Educational Material (MIT License)

**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c

</div>
