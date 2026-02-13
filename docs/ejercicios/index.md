# Ejercicios

Lista completa de todos los ejercicios disponibles en el curso.

---

## Roadmap de Ejercicios

<<<<<<< HEAD
### Módulo 1: Bases de Datos

| # | Ejercicio | Tecnología | Nivel | Tiempo | Estado |
|---|-----------|------------|-------|--------|--------|
| 1.1 | Introducción SQLite | SQLite + Pandas | 🟢 Básico | 8-10h | ✅ Disponible |
| 2.1 | PostgreSQL HR | PostgreSQL | 🟡 Intermedio | 4-6h | 🚧 Próximo |
| 2.2 | PostgreSQL Jardinería | PostgreSQL | 🟡 Intermedio | 4-6h | 🚧 Próximo |
| 2.3 | Migración SQLite → PostgreSQL | PostgreSQL + Python | 🟡 Intermedio | 3-4h | 🚧 Próximo |
| 3.1 | Oracle HR | Oracle Database | 🔴 Avanzado | 5-7h | 🚧 Próximo |
| 3.2 | Oracle Jardinería | Oracle Database | 🔴 Avanzado | 4-5h | 🚧 Próximo |
| 4.1 | SQL Server Tienda | SQL Server | 🔴 Avanzado | 4-5h | 🚧 Próximo |
| 5.1 | Análisis Excel/Python | Pandas + Excel | 🟢 Básico | 3-4h | 🚧 Próximo |

### Módulo 2: Big Data (Próximamente)

| # | Ejercicio | Tecnología | Nivel | Tiempo | Estado |
|---|-----------|------------|-------|--------|--------|
| 02 | Limpieza de Datos | Pandas | 🟢 Básico | 3-4h | 📅 Planificado |
| 03 | Parquet y Dask | Dask + Parquet | 🟡 Intermedio | 4-5h | 📅 Planificado |
| 04 | PySpark Queries | PySpark | 🔴 Avanzado | 5-6h | 📅 Planificado |
| 05 | Dashboard Interactivo | Flask + Chart.js | 🔴 Avanzado | 8-10h | 📅 Planificado |
| 06 | Pipeline ETL | Dask + PySpark | 🔴 Avanzado | 10-12h | 📅 Planificado |

---

## MÓDULO 1: Bases de Datos

### [Ejercicio 1.1: Introducción a SQLite](01-introduccion-sqlite.md)

!!! info "Detalles"
    - **Nivel:** 🟢 Basico
    - **Tiempo:** 2-3 horas
=======
### Modulo 1: Bases de Datos

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 1.1 | [Introduccion SQLite](01-introduccion-sqlite.md) | SQLite + Pandas | Basico | Disponible |
| 2.1 | [PostgreSQL HR](02-postgresql-hr.md) | PostgreSQL | Intermedio | Disponible |
| 2.2 | [PostgreSQL Jardineria](03-postgresql-jardineria.md) | PostgreSQL | Intermedio | Disponible |
| 2.3 | [Migracion SQLite a PostgreSQL](04-migracion-sqlite-postgresql.md) | PostgreSQL + Python | Intermedio | Disponible |
| 3.1 | [Oracle HR](05-oracle-hr.md) | Oracle Database | Avanzado | Disponible |
| 5.1 | [Analisis Excel/Python](06-analisis-excel-python.md) | Pandas + Excel | Basico | Disponible |

### Modulo 2: Limpieza de Datos y ETL

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 02 | [Pipeline ETL QoG](02-pipeline-etl-qog.md) | PostgreSQL + Pandas | Avanzado | Disponible |

### Modulo 3: Procesamiento Distribuido

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 03 | [Procesamiento Distribuido con Dask](03-procesamiento-distribuido.md) | Dask + Parquet | Intermedio | Disponible |

### Modulo 4: Machine Learning

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 04 | [Machine Learning (PCA, K-Means)](04-machine-learning.md) | Scikit-Learn, PCA, K-Means | Avanzado | Disponible |
| 04.2 | [Transfer Learning Flores](04-machine-learning.md#ejercicio-42-transfer-learning-clasificacion-de-flores) | TensorFlow, MobileNetV2 | Avanzado | Disponible |
| ARIMA | [Series Temporales ARIMA/SARIMA](07-series-temporales-arima.md) | statsmodels, Box-Jenkins | Avanzado | Disponible |

### Modulo 5: NLP y Text Mining

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 05 | [NLP y Text Mining](05-nlp-mining.md) | NLTK, TF-IDF, Jaccard, Sentimiento | Avanzado | Disponible |

### Modulo 6: Analisis de Datos de Panel

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 06 | [Analisis de Datos de Panel](08-panel-data.md) | linearmodels, Panel OLS, Altair | Avanzado | Disponible |

### Modulo 7: Infraestructura Big Data

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 07 | [Infraestructura Big Data](07-infraestructura-bigdata.md) | Docker Compose, Apache Spark | Intermedio-Avanzado | Disponible |

### Modulo 8: Streaming con Kafka

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 08 | [Streaming con Kafka](08-streaming-kafka.md) | Apache Kafka, Spark Streaming, KRaft | Avanzado | Disponible |

### Modulo 9: Cloud con LocalStack

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| 09 | [Cloud con LocalStack](09-cloud-localstack.md) | LocalStack, Terraform, AWS | Avanzado | Disponible |

### Trabajo Final

| # | Ejercicio | Tecnologia | Nivel | Estado |
|---|-----------|------------|-------|--------|
| TF | [Proyecto Final Integrador](06-trabajo-final-capstone.md) | Docker + Spark + PostgreSQL + QoG | Avanzado | Disponible |

---

## MODULO 1: Bases de Datos

### [Ejercicio 1.1: Introduccion a SQLite](01-introduccion-sqlite.md)

!!! info "Detalles"
    - **Nivel:** Basico
>>>>>>> upstream/main
    - **Dataset:** NYC Taxi (muestra 10MB)
    - **Tecnologias:** SQLite, Pandas

**Que aprenderas:**

- Cargar datos CSV a base de datos SQLite
- Queries SQL basicas (SELECT, WHERE, GROUP BY)
- Optimizacion con indices
- Exportar resultados a CSV

<<<<<<< HEAD
**Objetivos:**

- [x] Cargar CSV en chunks
- [x] Crear base de datos SQLite
- [x] Ejecutar queries SQL
- [x] Crear indices para optimizacion
- [x] Exportar resultados

[Ver Ejercicio Completo →](01-introduccion-sqlite.md){ .md-button .md-button--primary }
=======
[Ver Ejercicio Completo](01-introduccion-sqlite.md){ .md-button .md-button--primary }
>>>>>>> upstream/main

---

### [Ejercicio 2.1: PostgreSQL con BD HR](02-postgresql-hr.md)

!!! info "Detalles"
<<<<<<< HEAD
    - **Nivel:** 🟡 Intermedio
    - **Tiempo:** 4-6 horas
    - **Base de Datos:** HR (Human Resources) de Oracle
    - **Tecnologías:** PostgreSQL, SQL

**Qué aprenderás:**

- Instalar y configurar PostgreSQL
- Cargar bases de datos desde scripts SQL
- Consultas complejas con múltiples JOINs
- Funciones específicas de PostgreSQL
- Comparar Oracle vs PostgreSQL

[Ver Ejercicio Completo →](02-postgresql-hr.md){ .md-button }

---

### [Ejercicio 2.2: PostgreSQL Jardinería](03-postgresql-jardineria.md)

!!! info "Detalles"
    - **Nivel:** 🟡 Intermedio
    - **Tiempo:** 4-6 horas
    - **Base de Datos:** Sistema de ventas de jardinería
    - **Tecnologías:** PostgreSQL, Window Functions

**Qué aprenderás:**

- Análisis de ventas con SQL
- Agregaciones complejas (GROUP BY, HAVING)
- Window Functions para rankings
- Optimización con índices
- Vistas materializadas

[Ver Ejercicio Completo →](03-postgresql-jardineria.md){ .md-button }

---

### [Ejercicio 2.3: Migración SQLite → PostgreSQL](04-migracion-sqlite-postgresql.md)

!!! info "Detalles"
    - **Nivel:** 🟡 Intermedio
    - **Tiempo:** 3-4 horas
    - **Tecnologías:** SQLite, PostgreSQL, Python

**Qué aprenderás:**
=======
    - **Nivel:** Intermedio
    - **Base de Datos:** HR (Human Resources) de Oracle
    - **Tecnologias:** PostgreSQL, SQL

**Que aprenderas:**

- Instalar y configurar PostgreSQL
- Cargar bases de datos desde scripts SQL
- Consultas complejas con multiples JOINs
- Funciones especificas de PostgreSQL

[Ver Ejercicio Completo](02-postgresql-hr.md){ .md-button }

---

### [Ejercicio 2.2: PostgreSQL Jardineria](03-postgresql-jardineria.md)

!!! info "Detalles"
    - **Nivel:** Intermedio
    - **Base de Datos:** Sistema de ventas de jardineria
    - **Tecnologias:** PostgreSQL, Window Functions

**Que aprenderas:**

- Analisis de ventas con SQL
- Agregaciones complejas (GROUP BY, HAVING)
- Window Functions para rankings
- Vistas materializadas

[Ver Ejercicio Completo](03-postgresql-jardineria.md){ .md-button }

---

### [Ejercicio 2.3: Migracion SQLite a PostgreSQL](04-migracion-sqlite-postgresql.md)

!!! info "Detalles"
    - **Nivel:** Intermedio
    - **Tecnologias:** SQLite, PostgreSQL, Python

**Que aprenderas:**
>>>>>>> upstream/main

- Diferencias entre motores de BD
- Migrar esquemas y datos
- Adaptar tipos de datos
- Validar integridad
<<<<<<< HEAD
- Comparar rendimiento

[Ver Ejercicio Completo →](04-migracion-sqlite-postgresql.md){ .md-button }
=======

[Ver Ejercicio Completo](04-migracion-sqlite-postgresql.md){ .md-button }
>>>>>>> upstream/main

---

### [Ejercicio 3.1: Oracle con BD HR](05-oracle-hr.md)

!!! warning "Avanzado"
<<<<<<< HEAD
    - **Nivel:** 🔴 Avanzado
    - **Tiempo:** 5-7 horas
    - **Base de Datos:** HR en Oracle nativo
    - **Tecnologías:** Oracle Database, PL/SQL

**Qué aprenderás:**

- Instalar Oracle Database XE
- Sintaxis específica de Oracle
- PL/SQL (procedimientos, funciones)
- Secuencias y triggers
- Comparar con PostgreSQL

[Ver Ejercicio Completo →](05-oracle-hr.md){ .md-button }

---

### [Ejercicio 5.1: Análisis Excel/Python](06-analisis-excel-python.md)

!!! info "Detalles"
    - **Nivel:** 🟢 Básico-Intermedio
    - **Tiempo:** 3-4 horas
    - **Tecnologías:** Python, Pandas, Excel

**Qué aprenderás:**

- Leer archivos Excel con Python
- Análisis exploratorio de datos (EDA)
- Visualizaciones con matplotlib/seaborn
- Automatizar análisis
- Comparar manual vs programático

[Ver Ejercicio Completo →](06-analisis-excel-python.md){ .md-button }

---

## MÓDULO 2: Big Data

### Ejercicio 02: Limpieza y Transformacion

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Detectar y manejar valores nulos
- Identificar y tratar outliers
- Transformaciones de datos
- Validacion de tipos de datos
- Normalizacion y estandarizacion

---

### Ejercicio 03: Procesamiento con Parquet y Dask

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Por que Parquet es mejor que CSV
- Procesamiento paralelo con Dask
- Lazy evaluation
- Optimizacion de memoria
- Comparativa de rendimiento

---

### Ejercicio 04: Queries Complejas con PySpark

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Introduccion a Apache Spark
- DataFrames distribuidos
- SQL en Spark
- Joins de multiples fuentes
- Particionamiento de datos

---

### Ejercicio 05: Dashboard Interactivo

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Flask para backend
- Chart.js para visualizaciones
- Conectar frontend con analisis
- Deploy local con Docker
- Optimizacion de rendimiento

---

### Ejercicio 06: Pipeline ETL Completo

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Diseno de arquitectura ETL
- Extract con multiples fuentes
- Transform con Dask/PySpark
- Load a Parquet optimizado
- Monitoreo y logging
- Deploy a produccion
=======
    - **Nivel:** Avanzado
    - **Base de Datos:** HR en Oracle nativo
    - **Tecnologias:** Oracle Database, PL/SQL

**Que aprenderas:**

- Instalar Oracle Database XE
- Sintaxis especifica de Oracle
- PL/SQL (procedimientos, funciones)
- Secuencias y triggers

[Ver Ejercicio Completo](05-oracle-hr.md){ .md-button }

---

### [Ejercicio 5.1: Analisis Excel/Python](06-analisis-excel-python.md)

!!! info "Detalles"
    - **Nivel:** Basico-Intermedio
    - **Tecnologias:** Python, Pandas, Excel

**Que aprenderas:**

- Leer archivos Excel con Python
- Analisis exploratorio de datos (EDA)
- Visualizaciones con matplotlib/seaborn
- Automatizar analisis

[Ver Ejercicio Completo](06-analisis-excel-python.md){ .md-button }

---

## MODULO 2: Limpieza de Datos y ETL

### [Pipeline ETL Profesional - Quality of Government](02-pipeline-etl-qog.md)

!!! info "Detalles"
    - **Nivel:** Avanzado
    - **Dataset:** QoG (1289 variables, 194+ paises)
    - **Tecnologias:** PostgreSQL, Pandas, psycopg2

**Que aprenderas:**

- Disenar arquitectura ETL modular
- Trabajar con PostgreSQL para analisis longitudinal
- Limpiar datasets complejos (>1000 variables)
- Preparar datos de panel para econometria

[Ver Ejercicio Completo](02-pipeline-etl-qog.md){ .md-button }

---

## MODULO 3: Procesamiento Distribuido

### [Procesamiento Distribuido con Dask](03-procesamiento-distribuido.md)

!!! info "Detalles"
    - **Nivel:** Intermedio
    - **Tecnologias:** Dask, Parquet, LocalCluster

**Que aprenderas:**

- Configurar un Cluster Local con Dask
- Leer archivos Parquet de forma particionada
- Ejecutar agregaciones complejas en paralelo
- Comparar rendimiento vs Pandas

[Ver Ejercicio Completo](03-procesamiento-distribuido.md){ .md-button }

---

## MODULO 4: Machine Learning

### [Machine Learning en Big Data](04-machine-learning.md)

!!! info "Detalles"
    - **Nivel:** Avanzado
    - **Tecnologias:** Scikit-Learn, PCA, K-Means
    - **Scripts:** PCA Iris, FactoMineR, Breast Cancer, Wine, TF-IDF

**Que aprenderas:**

- Reduccion de dimensionalidad con PCA
- Clustering con K-Means y Hierarchical Clustering
- Interpretacion de componentes principales
- Perfilado de clusters

[Ver Ejercicio Completo](04-machine-learning.md){ .md-button }

---

### [Transfer Learning: Clasificacion de Flores](04-machine-learning.md#ejercicio-42-transfer-learning-clasificacion-de-flores)

!!! info "Detalles"
    - **Nivel:** Avanzado
    - **Tecnologias:** TensorFlow, MobileNetV2, Scikit-Learn
    - **Dataset:** TensorFlow Flowers (3,670 imagenes, 5 clases)

**Que aprenderas:**

- Transfer Learning con redes pre-entrenadas (ImageNet)
- Extraccion de embeddings con CNNs
- Clasificacion de imagenes con ML tradicional (KNN, SVM, Random Forest)
- Visualizacion t-SNE de espacios de alta dimension

[Ver Dashboard Interactivo](../dashboards/dashboard_flores.html){ .md-button target="_blank" }

---

### [Series Temporales: ARIMA/SARIMA](07-series-temporales-arima.md)

!!! info "Detalles"
    - **Nivel:** Avanzado
    - **Dataset:** AirPassengers (144 observaciones, 1949-1960)
    - **Tecnologias:** statsmodels, Metodologia Box-Jenkins

**Que aprenderas:**

- Metodologia Box-Jenkins completa (Identificacion, Estimacion, Diagnostico, Pronostico)
- Modelos ARIMA y SARIMA con estacionalidad
- ACF/PACF para identificacion de ordenes
- Diagnostico de residuos y pronosticos

[Ver Ejercicio Completo](07-series-temporales-arima.md){ .md-button }

---

---

## MODULO 5: NLP y Text Mining

### [NLP y Text Mining](05-nlp-mining.md)

!!! info "Detalles"
    - **Nivel:** Avanzado
    - **Tecnologias:** NLTK, TF-IDF, Jaccard, Sentiment Analysis
    - **Scripts:** Conteo, Limpieza, Sentimiento, Similitud

**Que aprenderas:**

- Tokenizacion y limpieza de texto
- Eliminacion de stopwords
- Similitud de Jaccard entre documentos
- Analisis de sentimiento por lexicon

[Ver Ejercicio Completo](05-nlp-mining.md){ .md-button }

---

## MODULO 6: Analisis de Datos de Panel

### [Analisis de Datos de Panel](08-panel-data.md)

!!! info "Detalles"
    - **Nivel:** Avanzado
    - **Datasets:** Guns (leyes de armas), Fatalities (mortalidad trafico)
    - **Tecnologias:** linearmodels, Panel OLS, Altair

**Que aprenderas:**

- Datos de panel: estructura pais x anio
- Efectos Fijos vs Efectos Aleatorios
- Two-Way Fixed Effects
- Test de Hausman para seleccion de modelo
- Odds Ratios y Efectos Marginales

[Ver Ejercicio Completo](08-panel-data.md){ .md-button }

---

## MODULO 7: Infraestructura Big Data

### [Infraestructura Big Data: Docker y Spark](07-infraestructura-bigdata.md)

!!! info "Detalles"
    - **Nivel:** Intermedio-Avanzado
    - **Tipo:** Teorico-Conceptual con ejemplos practicos
    - **Tecnologias:** Docker, Docker Compose, Apache Spark

**Que aprenderas:**

- Docker: contenedores, imagenes, Dockerfile, orquestacion con Compose
- Redes, volumenes, healthchecks, patrones de produccion
- Apache Spark: arquitectura Master-Worker, cluster con Docker
- SparkSession, Lazy Evaluation, DAG, optimizador Catalyst
- Spark + PostgreSQL via JDBC
- De Standalone a produccion (Kubernetes, EMR, Dataproc)

[Ver Ejercicio Completo](07-infraestructura-bigdata.md){ .md-button }

---

## MODULO 8: Streaming con Kafka

### [Streaming con Apache Kafka](08-streaming-kafka.md)

!!! info "Detalles"
    - **Nivel:** Avanzado
    - **Tecnologias:** Apache Kafka (KRaft), Python, Spark Streaming
    - **API:** USGS Earthquakes (tiempo real)

**Que aprenderas:**

- Arquitectura de Kafka: Brokers, Topics, Partitions
- Modo KRaft (sin ZooKeeper)
- Productores y Consumidores en Python
- Spark Structured Streaming
- Sistema de alertas en tiempo real

[Ver Ejercicio Completo](08-streaming-kafka.md){ .md-button }

---

## MODULO 9: Cloud con LocalStack

### [Cloud con LocalStack y Terraform](09-cloud-localstack.md)

!!! info "Detalles"
    - **Nivel:** Avanzado
    - **Tecnologias:** LocalStack, Terraform, AWS (S3, Lambda, DynamoDB)
    - **API:** ISS Tracker (tiempo real)

**Que aprenderas:**

- Cloud Computing: IaaS, PaaS, SaaS
- Simular AWS localmente con LocalStack
- Infraestructura como Codigo con Terraform
- Funciones Lambda serverless
- Arquitectura Data Lake (Medallion)

[Ver Ejercicio Completo](09-cloud-localstack.md){ .md-button }

---

## TRABAJO FINAL

### [Proyecto Final: Pipeline de Big Data con Docker](06-trabajo-final-capstone.md)

!!! success "Proyecto Integrador"
    - **Nivel:** Avanzado
    - **Tecnologias:** Docker, Apache Spark, PostgreSQL, QoG
    - **Evaluacion:** Infraestructura 30% + ETL 25% + Analisis 25% + Reflexion IA 20%

**Que haras:**

- Construir infraestructura Docker (Spark + PostgreSQL)
- Disenar y ejecutar un pipeline ETL con Apache Spark
- Analizar datos QoG con pregunta de investigacion propia
- Documentar tu proceso de aprendizaje con IA

[Ver Enunciado Completo](06-trabajo-final-capstone.md){ .md-button .md-button--primary }
>>>>>>> upstream/main

---

## Datasets Utilizados

### NYC Taxi & Limousine Commission (TLC)

- **Fuente:** [NYC Open Data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Periodo:** 2021
<<<<<<< HEAD
- **Tamano:** 121 MB (muestra), varios GB (completo)
- **Registros:** 10M+ viajes

**Campos principales:**

- `tpep_pickup_datetime`: Fecha/hora de inicio
- `tpep_dropoff_datetime`: Fecha/hora de fin
- `passenger_count`: Numero de pasajeros
- `trip_distance`: Distancia en millas
- `total_amount`: Tarifa total
- `payment_type`: Metodo de pago

### Weather Data (NOAA)

!!! info "Uso en Ejercicio 04"
    Combinado con datos de taxi para analisis avanzados

- **Fuente:** NOAA Weather Database
- **Variables:** Temperatura, precipitacion, viento
- **Uso:** Join con datos de taxi para analisis de impacto del clima
=======
- **Registros:** 10M+ viajes

### Quality of Government (QoG)

- **Fuente:** [Universidad de Gotemburgo](https://www.qog.pol.gu.se/)
- **Variables:** 1289 indicadores de calidad institucional
- **Paises:** 194+ con datos desde 1946

### AirPassengers

- **Fuente:** Box & Jenkins (1976)
- **Periodo:** 1949-1960 (144 observaciones mensuales)
- **Uso:** Series temporales ARIMA/SARIMA
>>>>>>> upstream/main

---

## Como Trabajar los Ejercicios

### Flujo Recomendado

1. **Leer el enunciado completo** - No empieces a codear sin leer todo
2. **Entender los objetivos** - Que se espera que logres?
3. **Crear rama de trabajo** - `git checkout -b tu-apellido-ejercicio-XX`
4. **Trabajar en pasos pequenos** - No intentes hacerlo todo de una vez
5. **Probar frecuentemente** - Ejecuta tu codigo cada vez que completes una parte
6. **Hacer commits regulares** - Guarda tu progreso frecuentemente
<<<<<<< HEAD
7. **Crear Pull Request** - Cuando completes el ejercicio

### Mejores Practicas

!!! tip "Consejos para el Exito"

    - **No copiar y pegar sin entender** - Escribe el codigo tu mismo
    - **Leer los errores** - Los mensajes de error te dicen que esta mal
    - **Usar print() para debug** - Imprime variables para ver su contenido
    - **Comentar tu codigo** - Explica que hace cada parte
    - **Pedir ayuda si te atoras** - Pero intenta resolverlo primero

---

## Evaluacion

### Criterios de Evaluacion

Los ejercicios se evaluan basandose en:

1. **Funcionalidad** (40%)
    - El codigo ejecuta sin errores?
    - Cumple con todos los objetivos?
    - Los resultados son correctos?

2. **Codigo Limpio** (30%)
    - Es legible?
    - Esta bien documentado?
    - Sigue buenas practicas?

3. **Rendimiento** (20%)
    - Esta optimizado?
    - Usa memoria eficientemente?
    - Tiempo de ejecucion razonable?

4. **Creatividad** (10%)
    - Agrega analisis adicionales?
    - Propone mejoras?
    - Resuelve de forma innovadora?

### Rubrica

| Criterio | Excelente (100%) | Bueno (80%) | Suficiente (60%) | Insuficiente (<60%) |
|----------|------------------|-------------|------------------|---------------------|
| **Funcionalidad** | Cumple todos los objetivos sin errores | Cumple objetivos con errores menores | Cumple parcialmente | No funciona |
| **Codigo** | Muy legible, bien documentado | Legible, documentacion basica | Poco legible | Ilegible |
| **Rendimiento** | Optimizado | Funcional | Lento pero funciona | Muy lento |
| **Creatividad** | Analisis adicionales innovadores | Algunas mejoras | Basico | Solo lo minimo |

---

## FAQ de Ejercicios

??? question "Puedo usar librerias adicionales?"

    Si, pero:

    - Justifica por que las necesitas
    - Agregalas a `requirements.txt`
    - Documenta como instalarlas

??? question "Cuanto tiempo debo dedicar a cada ejercicio?"

    Los tiempos son estimados:

    - **Principiantes:** Pueden tomar el doble
    - **Intermedios:** El tiempo estimado
    - **Avanzados:** La mitad del tiempo

    No hay prisa. Aprende bien cada concepto.

??? question "Que hago si me atorο?"

    1. Lee el error cuidadosamente
    2. Busca en Google el mensaje de error
    3. Revisa la documentacion de la libreria
    4. Pregunta en el PR con `@TodoEconometria`
    5. Alumnos presenciales: Consulta en clase

??? question "Puedo hacer los ejercicios en desorden?"

    **No recomendado.** Los ejercicios estan disenados para:

    - Construir sobre conocimientos previos
    - Aumentar dificultad gradualmente
    - Introducir conceptos en orden logico

    Si ya tienes experiencia, puedes saltar niveles, pero no ejercicios dentro del mismo nivel.

---

## Recursos Adicionales

### Documentacion

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Dask Documentation](https://docs.dask.org/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)

### Tutoriales

- [Python for Data Analysis](https://wesmckinney.com/book/)
- [SQL for Data Science](https://mode.com/sql-tutorial/)
- [Dask Tutorial](https://tutorial.dask.org/)
=======
7. **Subir con git push** - Cuando completes, el sistema evalua tu PROMPTS.md
>>>>>>> upstream/main

---

## Proximos Pasos

Empieza con el primer ejercicio:

<<<<<<< HEAD
[Ejercicio 01: Introduccion SQLite →](01-introduccion-sqlite.md){ .md-button .md-button--primary }

O revisa:

- [Roadmap del Curso](../guia-inicio/roadmap.md) - Plan completo de estudio
- [Tu Primer Ejercicio](../guia-inicio/primer-ejercicio.md) - Flujo de trabajo
- [Crear Pull Requests](../git-github/pull-requests.md) - Como entregar ejercicios
=======
[Ejercicio 01: Introduccion SQLite](01-introduccion-sqlite.md){ .md-button .md-button--primary }

O salta al proyecto final:

[Trabajo Final: Pipeline Big Data](06-trabajo-final-capstone.md){ .md-button }
>>>>>>> upstream/main
