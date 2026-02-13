<<<<<<< HEAD
# Big Data con Python - De Cero a Produccion

> **Aprende a procesar millones de registros sin que tu computadora explote**
>
> Repositorio educativo completo para dominar Big Data con Python, desde conceptos basicos hasta produccion.

[![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)](https://github.com/TodoEconometria/ejercicios-bigdata/stargazers)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue)](https://www.linkedin.com/in/juangutierrezconsultor/)
[![Web](https://img.shields.io/badge/Web-TodoEconometria-orange)](https://www.todoeconometria.com)

---

## Que es Esto y Por Que Existe?

### El Problema

Imagina esto: Tienes un archivo Excel con **5 anos de ventas** (500,000 filas). Excel se congela. Python con Pandas se queda sin memoria. Tu jefe necesita el analisis **manana**.

**Te suena familiar?**

Este es el problema que enfrentan miles de analistas, cientificos de datos y empresas diariamente. Los datos crecen exponencialmente, pero las herramientas tradicionales no escalan.

### La Solucion

Este repositorio te ensena a:

```python
# ❌ Antes: Excel y Pandas basico
df = pd.read_csv("ventas_5_anos.csv")  # 💥 MemoryError
df.groupby("region").sum()              # 🐌 20 minutos

# ✅ Despues: Big Data con Python
df = dd.read_csv("ventas_5_anos.csv")  # ⚡ Carga lazy
df.groupby("region").sum().compute()    # 🚀 2 segundos
```

**Resultado:** Procesas 100GB de datos en tu laptop como si fueran 10MB.

### Por Que Este Repositorio

Este material surge de **230 horas de curso presencial** donde enseno Big Data a profesionales. He destilado:

- :white_check_mark: **10+ anos de experiencia** en analisis de datos
- :white_check_mark: **Errores comunes** que cometen los principiantes (y como evitarlos)
- :white_check_mark: **Mejores practicas** de la industria
- :white_check_mark: **Proyectos reales** adaptados para aprender

**No es solo teoria.** Cada ejercicio esta disenado para enfrentarte a problemas del mundo real.

---

## Para Quien es Este Repositorio?

=== "Alumnos del Curso Presencial"

    Si estas inscrito en mi curso presencial:

    - :white_check_mark: Este repo es tu **material de apoyo** completo
    - :white_check_mark: Aqui encontraras **todos los ejercicios** del curso
    - :white_check_mark: Puedes practicar **antes, durante y despues** de las clases
    - :white_check_mark: Tienes **soporte directo** en las sesiones presenciales

    !!! success "Ventaja"
        Mientras otros solo tienen diapositivas, tu tienes un repositorio completo con codigo ejecutable.

=== "Autodidactas y Curiosos"

    Si encontraste este repositorio por tu cuenta:

    - :white_check_mark: **Todo el contenido es gratuito** y de codigo abierto
    - :white_check_mark: Puedes aprender **a tu ritmo** sin presion
    - :white_check_mark: Practica con **ejercicios reales** de Big Data
    - :warning: **No incluye soporte** (solo para alumnos presenciales)

    !!! tip "Ventaja"
        Material profesional de calidad sin costo, perfecto para tu portafolio.

=== "Empresas y Profesionales"

    Si buscas soluciones para tu empresa:

    - :white_check_mark: **Portfolio real** de capacidades en Big Data
    - :white_check_mark: Muestra como **entreno equipos** profesionales
    - :white_check_mark: **Consultoria y capacitacion** in-company disponible
    - :white_check_mark: Proyectos de **analisis de datos a medida**

    !!! info "Ventaja"
        Ve exactamente que nivel de calidad ofrezco antes de contratarme.

---

## Que Aprenderas?

### Tecnologias que Dominaras

| Tecnologia | Que Hace | Cuando Usarla |
|------------|----------|---------------|
| **Python** | Lenguaje base | Siempre |
| **Pandas** | Datos en memoria (< 5GB) | Analisis exploratorio |
| **Dask** | Datos > RAM (5-100GB) | Datasets grandes en 1 maquina |
| **PySpark** | Datos masivos (> 100GB) | Clusters, produccion |
| **SQLite** | Base de datos embebida | Prototipos, proyectos pequenos |
| **Parquet** | Formato columnar | Almacenar datos procesados |
| **Git/GitHub** | Control de versiones | Todo proyecto profesional |
| **Flask** | Web framework | Dashboards, APIs |

### Ejemplos de Que Podras Hacer

!!! example "Ejemplo 1: Analizar 10 Millones de Viajes de Taxi"

    ```python
    # Dataset: NYC Taxi (121 MB CSV, 10M+ registros)
    # Pregunta: Cual es el ingreso promedio por hora del dia?

    import dask.dataframe as dd

    # Cargar 121 MB como si fueran 10 MB ⚡
    df = dd.read_csv("yellow_tripdata_2021-01.csv")

    # Analisis que en Pandas tomaria 5 minutos, aqui: 10 segundos
    resultado = (df.groupby(df['tpep_pickup_datetime'].dt.hour)
                  ['total_amount']
                  .mean()
                  .compute())

    print(resultado)
    # Resultado: Hora 23 es la mas rentable ($18.50 promedio)
    ```

!!! example "Ejemplo 2: Dashboard en Tiempo Real"

    Crear un dashboard interactivo que muestra:

    - :bar_chart: Distribucion de viajes por hora
    - :world_map: Mapa de calor de zonas mas rentables
    - :money_with_wings: Ingresos totales por dia/semana/mes
    - :chart_with_upwards_trend: Tendencias temporales

!!! example "Ejemplo 3: Pipeline ETL de Produccion"

    ```
    CSV (100GB) → Limpiar → Transformar → Parquet → Dashboard
                  (Dask)    (PySpark)    (10GB)     (Flask)
    ```

---

## Como Empezar?

!!! tip "Primera Vez con Git y Python?"
    Empieza con nuestra [Guia de Instalacion](guia-inicio/instalacion.md) donde te explicamos paso a paso como instalar todas las herramientas necesarias.

!!! info "Ya tienes Git y Python?"
    Ve directo a [Tu Primer Ejercicio](guia-inicio/primer-ejercicio.md) para comenzar a trabajar.

!!! warning "Desarrollador Experimentado?"
    Revisa el [Roadmap del Curso](guia-inicio/roadmap.md) para ver todos los ejercicios disponibles y elegir por donde empezar.

---

## Estadisticas del Repositorio

![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)
![GitHub forks](https://img.shields.io/github/forks/TodoEconometria/ejercicios-bigdata?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/TodoEconometria/ejercicios-bigdata?style=social)

---

## Servicios Profesionales

### Consultoria en Big Data

Necesitas ayuda con un proyecto de datos en tu empresa?

**Ofrezco:**

- :white_check_mark: **Desarrollo de Pipelines ETL/ELT** con Python y Spark
- :white_check_mark: **Capacitacion Empresarial** (cursos personalizados para tu equipo)
- :white_check_mark: **Analisis de Datos** para insights accionables
- :white_check_mark: **Automatizacion de Procesos** de datos
- :white_check_mark: **Migracion a Big Data** (de Excel/SQL a Dask/Spark)

!!! example "Casos de Uso"

    **Empresa A:** "Tenemos 5 anos de ventas en Excel y toma 2 horas generar reportes"

    → Solucion: Pipeline automatizado con Dask + Dashboard en tiempo real
    → Resultado: Reportes en 30 segundos

    **Empresa B:** "Queremos capacitar a 15 analistas en Big Data"

    → Solucion: Curso in-company de 40 horas adaptado a su industria
    → Resultado: Equipo autonomo procesando TB de datos

    **Startup C:** "Necesitamos procesar logs de servidores (1TB/dia)"

    → Solucion: Pipeline PySpark en AWS EMR
    → Resultado: Analisis en tiempo real con costos optimizados

### Contacto

:email: **Email:** [cursos@todoeconometria.com](mailto:cursos@todoeconometria.com)
:briefcase: **LinkedIn:** [Juan Gutierrez](https://www.linkedin.com/in/juangutierrezconsultor/)
:globe_with_meridians: **Web:** [www.todoeconometria.com](https://www.todoeconometria.com)
=======
# CURSO COMPLETO DE BIG DATA

<div style="text-align: center; padding: 30px 0;">
<img src="assets/todoeconometria_logo.png" alt="TodoEconometria" style="width: 350px; max-width: 80%;">
<p style="font-size: 1.3em; font-style: italic; color: #888; margin-top: 15px;">
"Sin experiencia no hay conocimiento"
</p>
</div>

<div style="text-align: center; margin: 20px 0;">
<a href="https://github.com/TodoEconometria/ejercicios-bigdata/stargazers"><img src="https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=for-the-badge&logo=github" alt="Stars"></a>
<a href="https://github.com/TodoEconometria/ejercicios-bigdata/network/members"><img src="https://img.shields.io/github/forks/TodoEconometria/ejercicios-bigdata?style=for-the-badge&logo=github" alt="Forks"></a>
<a href="https://www.linkedin.com/in/juangutierrezconsultor/"><img src="https://img.shields.io/badge/LinkedIn-Conectar-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"></a>
</div>

---

## Demos en Vivo

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 30px 0;">

<div style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 15px; padding: 25px; border: 1px solid #333;">
<h3 style="color: #ff6b6b; margin-top: 0;">Observatorio Sismico Global</h3>
<p style="color: #ccc;">Sismos en tiempo real desde USGS API. Mapa interactivo, filtros por magnitud, alertas de tsunami.</p>
<p style="margin-bottom: 0;">
<a href="dashboards/dashboard_sismos_global.html" target="_blank" style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 10px 25px; border-radius: 25px; text-decoration: none; font-weight: bold;">Ver en Vivo</a>
</p>
</div>

<div style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 15px; padding: 25px; border: 1px solid #333;">
<h3 style="color: #4facfe; margin-top: 0;">ISS Tracker</h3>
<p style="color: #ccc;">Rastrea la Estacion Espacial Internacional en tiempo real. Predictor de pases sobre tu ciudad.</p>
<p style="margin-bottom: 0;">
<a href="dashboards/dashboard_iss_tracker.html" target="_blank" style="background: linear-gradient(135deg, #00f2fe, #4facfe); color: white; padding: 10px 25px; border-radius: 25px; text-decoration: none; font-weight: bold;">Ver en Vivo</a>
</p>
</div>

</div>

<p style="text-align: center; color: #888; font-size: 0.9em;">
Estos dashboards se actualizan automaticamente con datos reales de APIs publicas
</p>

---

## El Curso en Numeros

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px; margin: 30px 0; text-align: center;">

<div style="background: #1e1e2e; border-radius: 10px; padding: 20px;">
<div style="font-size: 2.5em; font-weight: bold; color: #f39c12;">230</div>
<div style="color: #888;">Horas de contenido</div>
</div>

<div style="background: #1e1e2e; border-radius: 10px; padding: 20px;">
<div style="font-size: 2.5em; font-weight: bold; color: #3498db;">9</div>
<div style="color: #888;">Modulos completos</div>
</div>

<div style="background: #1e1e2e; border-radius: 10px; padding: 20px;">
<div style="font-size: 2.5em; font-weight: bold; color: #2ecc71;">25+</div>
<div style="color: #888;">Ejercicios practicos</div>
</div>

<div style="background: #1e1e2e; border-radius: 10px; padding: 20px;">
<div style="font-size: 2.5em; font-weight: bold; color: #9b59b6;">12+</div>
<div style="color: #888;">Dashboards interactivos</div>
</div>

<div style="background: #1e1e2e; border-radius: 10px; padding: 20px;">
<div style="font-size: 2.5em; font-weight: bold; color: #e74c3c;">30+</div>
<div style="color: #888;">Tecnologias</div>
</div>

</div>

---

## Stack Tecnologico Completo

### Bases de Datos

| Tecnologia | Nivel | Que Aprenderas |
|------------|-------|----------------|
| **SQLite** | Basico | Queries SQL, indices, optimizacion |
| **PostgreSQL** | Intermedio | Joins complejos, Window Functions, CTEs |
| **Oracle** | Avanzado | PL/SQL, procedimientos almacenados |
| **DynamoDB** | Avanzado | NoSQL, key-value, serverless |

### Procesamiento de Datos

| Tecnologia | Cuando Usarla | Escala |
|------------|---------------|--------|
| **Pandas** | Analisis exploratorio | < 5 GB |
| **Dask** | Datasets grandes, 1 maquina | 5-100 GB |
| **Apache Spark** | Clusters, produccion | > 100 GB |
| **Spark Streaming** | Datos en tiempo real | Ilimitado |

### Streaming y Mensajeria

| Tecnologia | Proposito |
|------------|-----------|
| **Apache Kafka** | Streaming distribuido, KRaft mode |
| **Spark Structured Streaming** | Procesamiento de streams |
| **AWS Kinesis** | Streaming en la nube |

### Cloud e Infraestructura

| Tecnologia | Que Hace |
|------------|----------|
| **Docker** | Contenedores, ambientes reproducibles |
| **Docker Compose** | Orquestacion multi-contenedor |
| **LocalStack** | Simulacion AWS local (gratis) |
| **Terraform** | Infraestructura como Codigo |
| **AWS S3** | Almacenamiento de objetos |
| **AWS Lambda** | Funciones serverless |
| **EventBridge** | Programacion de tareas |

### Machine Learning e IA

| Tecnologia | Aplicacion |
|------------|------------|
| **Scikit-learn** | ML clasico, clustering, clasificacion |
| **PCA** | Reduccion de dimensionalidad |
| **K-Means** | Segmentacion, clustering |
| **TensorFlow** | Deep Learning, redes neuronales |
| **MobileNetV2** | Transfer Learning, Computer Vision |
| **ARIMA/SARIMA** | Series temporales, forecasting |

### NLP y Text Mining

| Tecnologia | Uso |
|------------|-----|
| **NLTK** | Procesamiento de lenguaje natural |
| **TF-IDF** | Vectorizacion de texto |
| **Sentiment Analysis** | Analisis de sentimiento |
| **Jaccard Similarity** | Similitud entre documentos |

### Visualizacion

| Tecnologia | Tipo |
|------------|------|
| **Plotly** | Dashboards interactivos |
| **Matplotlib** | Graficos estaticos |
| **Seaborn** | Visualizacion estadistica |
| **Leaflet.js** | Mapas interactivos |
| **Altair** | Graficos declarativos |

### Econometria

| Tecnologia | Aplicacion |
|------------|------------|
| **linearmodels** | Datos de panel |
| **Panel OLS** | Efectos fijos y aleatorios |
| **Hausman Test** | Seleccion de modelo |

---

## Modulos del Curso

### Modulo 1: Bases de Datos
> SQLite, PostgreSQL, Oracle, migraciones

Desde tu primera query SELECT hasta procedimientos almacenados en Oracle. Aprenderas a disenar esquemas, optimizar consultas y migrar entre motores.

[Ver Ejercicios](ejercicios/index.md#modulo-1-bases-de-datos){ .md-button }

---

### Modulo 2: Limpieza de Datos y ETL
> Pipeline ETL profesional, QoG Dataset, PostgreSQL

Construye un pipeline ETL modular que procesa el dataset Quality of Government (1,289 variables, 194+ paises). Limpieza, transformacion y carga en PostgreSQL.

[Ver Ejercicios](ejercicios/index.md#modulo-2-limpieza-de-datos-y-etl){ .md-button }

---

### Modulo 3: Procesamiento Distribuido
> Dask, Parquet, Cluster Local

Procesa datasets grandes sin necesidad de un cluster. Dask te permite escalar pandas a datos que no caben en memoria, usando Parquet y paralelismo local.

[Ver Ejercicios](ejercicios/index.md#modulo-3-procesamiento-distribuido){ .md-button }

---

### Modulo 4: Machine Learning
> PCA, K-Means, Transfer Learning, ARIMA/SARIMA

Reduccion de dimensionalidad, clustering, clasificacion de imagenes con TensorFlow y series temporales con metodologia Box-Jenkins. Todo con datasets reales.

[Ver Ejercicios](ejercicios/index.md#modulo-4-machine-learning){ .md-button }

---

### Modulo 5: NLP y Text Mining
> NLTK, TF-IDF, Jaccard, Sentiment Analysis

Tokenizacion, limpieza de texto, similitud entre documentos, analisis de sentimiento y vectorizacion con TF-IDF.

[Ver Ejercicios](ejercicios/index.md#modulo-5-nlp-y-text-mining){ .md-button }

---

### Modulo 6: Analisis de Datos de Panel
> Efectos Fijos, Efectos Aleatorios, Hausman Test

Analiza datos longitudinales (pais x ano). Replica estudios academicos reales sobre leyes de armas y mortalidad de trafico.

[Ver Ejercicios](ejercicios/index.md#modulo-6-analisis-de-datos-de-panel){ .md-button }

---

### Modulo 7: Infraestructura Big Data
> Docker, Docker Compose, Apache Spark, Cluster Computing

Entiende como se construye la infraestructura. Contenedores, orquestacion con Docker Compose, clusters Spark con arquitectura Master-Worker. La base para el Trabajo Final.

[Ver Ejercicios](ejercicios/index.md#modulo-7-infraestructura-big-data){ .md-button }

---

### Modulo 8: Streaming con Kafka
> Apache Kafka, KRaft, Spark Structured Streaming

Streaming en tiempo real con Kafka (modo KRaft, sin ZooKeeper). Productores, consumidores, Spark Structured Streaming y sistema de alertas sismicas.

[Ver Ejercicios](ejercicios/index.md#modulo-8-streaming-con-kafka){ .md-button }

---

### Modulo 9: Cloud con LocalStack
> LocalStack, Terraform, AWS (S3, Lambda, DynamoDB)

Simula AWS en tu maquina sin costos. Infraestructura como Codigo con Terraform, funciones Lambda serverless y arquitectura Data Lake.

[Ver Ejercicios](ejercicios/index.md#modulo-9-cloud-con-localstack){ .md-button }

---

### Trabajo Final
> Docker + Spark + PostgreSQL + Analisis Completo

Integra todo lo aprendido en un proyecto de principio a fin. Infraestructura con Docker, ETL con Spark, analisis con tu pregunta de investigacion.

[Ver Enunciado](ejercicios/06-trabajo-final-capstone.md){ .md-button .md-button--primary }

---

## Galeria de Dashboards

Todos estos dashboards fueron creados durante el curso:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin: 20px 0;">

<div style="background: #1e1e2e; border-radius: 10px; padding: 15px; text-align: center;">
<strong style="color: #f39c12;">ARIMA PRO</strong><br>
<span style="color: #888; font-size: 0.9em;">Series temporales estilo Bloomberg</span><br>
<a href="dashboards/dashboard_arima_pro.html" target="_blank">Ver Dashboard</a>
</div>

<div style="background: #1e1e2e; border-radius: 10px; padding: 15px; text-align: center;">
<strong style="color: #3498db;">PCA + K-Means</strong><br>
<span style="color: #888; font-size: 0.9em;">Clustering y reduccion dimensional</span><br>
<a href="dashboards/02_pca_iris_dashboard.html" target="_blank">Ver Dashboard</a>
</div>

<div style="background: #1e1e2e; border-radius: 10px; padding: 15px; text-align: center;">
<strong style="color: #2ecc71;">Transfer Learning</strong><br>
<span style="color: #888; font-size: 0.9em;">Clasificacion de flores con CNN</span><br>
<a href="dashboards/dashboard_flores.html" target="_blank">Ver Dashboard</a>
</div>

<div style="background: #1e1e2e; border-radius: 10px; padding: 15px; text-align: center;">
<strong style="color: #9b59b6;">Panel Data QoG</strong><br>
<span style="color: #888; font-size: 0.9em;">Spark + PostgreSQL + ML</span><br>
<a href="dashboards/06_analisis_panel_qog.html" target="_blank">Ver Dashboard</a>
</div>

</div>

[Ver Todos los Dashboards](dashboards/index.md){ .md-button }

---

## Para Quien es Este Curso?

=== "Estudiantes y Autodidactas"

    - Todo el contenido es **gratuito** y open source
    - Aprende a tu ritmo con ejercicios progresivos
    - Construye un **portfolio profesional** de proyectos
    - Dashboards reales que puedes mostrar en entrevistas

=== "Profesionales en Activo"

    - Actualiza tus skills a tecnologias modernas
    - De Excel a Spark en semanas, no anos
    - Streaming, Cloud, ML - todo en un solo curso
    - Aplicable inmediatamente en tu trabajo

=== "Empresas"

    - Capacitacion in-company disponible
    - Material probado en 230+ horas de clase presencial
    - Casos de uso reales de la industria
    - Consultoria para proyectos especificos

---

## Como Empezar

!!! warning "Alumnos del Curso Presencial"
    Lee primero la [Guia de Entregas](entregas/guia-entregas.md) para saber como entregar tus trabajos.

### Paso 1: Fork y Clone

```bash
# Haz fork en GitHub (boton arriba a la derecha)
# Luego clona TU fork:
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
```

### Paso 2: Instala Dependencias

```bash
pip install -r requirements.txt
```

### Paso 3: Elige tu Camino

| Si eres... | Empieza con... |
|------------|----------------|
| **Principiante** | [Ejercicio 1.1: SQLite](ejercicios/01-introduccion-sqlite.md) |
| **Intermedio** | [Pipeline ETL QoG](ejercicios/02-pipeline-etl-qog.md) |
| **Avanzado** | [Streaming con Kafka](ejercicios/08-streaming-kafka.md) |

---

## Instructor

<div style="display: flex; align-items: center; gap: 20px; margin: 20px 0;">
<div>
<strong style="font-size: 1.2em;">Juan Marcelo Gutierrez Miranda</strong><br>
<span style="color: #888;">@TodoEconometria</span><br><br>
10+ anos en analisis de datos y Big Data. He formado a cientos de profesionales en empresas de toda Latinoamerica y Espana.
</div>
</div>

### Servicios Profesionales

- **Capacitacion In-Company**: Cursos adaptados a tu equipo y tecnologias
- **Consultoria Big Data**: Diseno de pipelines, arquitectura de datos
- **Desarrollo de Dashboards**: Visualizaciones interactivas para tu negocio

**Contacto:**

- **Email:** [cursos@todoeconometria.com](mailto:cursos@todoeconometria.com)
- **LinkedIn:** [Juan Gutierrez](https://www.linkedin.com/in/juangutierrezconsultor/)
- **Web:** [www.todoeconometria.com](https://www.todoeconometria.com)
>>>>>>> upstream/main

---

## Contribuciones

<<<<<<< HEAD
Este repositorio esta en constante evolucion. Si encuentras:

- :bug: Errores o bugs
- :pencil: Mejoras en la documentacion
- :bulb: Ideas para nuevos ejercicios
- :art: Ejemplos de dashboards

!!! tip "Crea un Issue o Pull Request"
    1. Fork este repositorio
    2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
    3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
    4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
    5. Abre un Pull Request

---

## Licencia

Este proyecto esta bajo la Licencia MIT - ver el archivo [LICENSE](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/LICENSE) para detalles.

**En resumen:** Puedes usar este material para aprender, ensenar, o modificar, siempre que des credito.

---

## Listo para Empezar?

```bash
# 1. Haz fork de este repositorio (boton arriba a la derecha)

# 2. Clona TU fork
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# 3. Instala dependencias
cd ejercicios-bigdata
pip install -r requirements.txt

# 4. Empieza con el Ejercicio 01
cd ejercicios
python 01_cargar_sqlite.py

# 5. Aprende, practica, crece!
```

---

<p align="center">
  <b>Tu carrera en Big Data empieza aqui.</b><br>
  Preguntas? Abre un <a href="https://github.com/TodoEconometria/ejercicios-bigdata/issues">Issue</a> o contactame en <a href="https://www.linkedin.com/in/juangutierrezconsultor/">LinkedIn</a>
</p>

<p align="center">
  Hecho con ❤️ por <a href="https://www.todoeconometria.com">TodoEconometria</a>
=======
Este repositorio es open source. Si encuentras errores o quieres contribuir:

1. Haz fork del repositorio
2. Crea una rama para tu cambio
3. Envia un Pull Request

---

<div style="text-align: center; padding: 40px 0; background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 15px; margin: 30px 0;">
<h2 style="margin-top: 0;">Tu Carrera en Big Data Empieza Aqui</h2>
<p style="color: #888; margin-bottom: 25px;">230 horas de contenido, 30+ tecnologias, dashboards en tiempo real</p>
<a href="ejercicios/" style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 15px 40px; border-radius: 30px; text-decoration: none; font-size: 1.1em; font-weight: bold;">Comenzar Ahora</a>
</div>

---

<p style="text-align: center; color: #666;">
<strong>Curso:</strong> Big Data con Python - De Cero a Produccion<br>
<strong>Profesor:</strong> Juan Marcelo Gutierrez Miranda | @TodoEconometria<br>
<strong>Hash ID:</strong> 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
>>>>>>> upstream/main
</p>
