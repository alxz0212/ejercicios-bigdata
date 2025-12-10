# 🚀 Big Data con Python - De Cero a Producción

> **Aprende a procesar millones de registros sin que tu computadora explote**
> Repositorio educativo completo para dominar Big Data con Python, desde conceptos básicos hasta producción.

[![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)](https://github.com/TodoEconometria/ejercicios-bigdata/stargazers)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue)](https://www.linkedin.com/in/juangutierrezconsultor/)
[![Web](https://img.shields.io/badge/Web-TodoEconometria-orange)](https://www.todoeconometria.com)

---

## 🎯 ¿Qué es Esto y Por Qué Existe?

### El Problema

Imagina esto: Tienes un archivo Excel con **5 años de ventas** (500,000 filas). Excel se congela. Python con Pandas se queda sin memoria. Tu jefe necesita el análisis **mañana**.

**¿Te suena familiar?**

Este es el problema que enfrentan miles de analistas, científicos de datos y empresas diariamente. Los datos crecen exponencialmente, pero las herramientas tradicionales no escalan.

### La Solución

Este repositorio te enseña a:

```python
# ❌ Antes: Excel y Pandas básico
df = pd.read_csv("ventas_5_años.csv")  # 💥 MemoryError
df.groupby("región").sum()              # 🐌 20 minutos

# ✅ Después: Big Data con Python
df = dd.read_csv("ventas_5_años.csv")  # ⚡ Carga lazy
df.groupby("región").sum().compute()    # 🚀 2 segundos
```

**Resultado:** Procesas 100GB de datos en tu laptop como si fueran 10MB.

### Por Qué Este Repositorio

Este material surge de **230 horas de curso presencial** donde enseño Big Data a profesionales. He destilado:

- ✅ **10+ años de experiencia** en análisis de datos
- ✅ **Errores comunes** que cometen los principiantes (y cómo evitarlos)
- ✅ **Mejores prácticas** de la industria
- ✅ **Proyectos reales** adaptados para aprender

**No es solo teoría.** Cada ejercicio está diseñado para enfrentarte a problemas del mundo real.

---

## 👥 ¿Para Quién es Este Repositorio?

<details>
<summary><b>🎓 Alumnos del Curso Presencial (230 horas)</b></summary>

Si estás inscrito en mi curso presencial:

- ✅ Este repo es tu **material de apoyo** completo
- ✅ Aquí encontrarás **todos los ejercicios** del curso
- ✅ Puedes practicar **antes, durante y después** de las clases
- ✅ Tienes **soporte directo** en las sesiones presenciales

**Ventaja:** Mientras otros solo tienen diapositivas, tú tienes un repositorio completo con código ejecutable.

</details>

<details>
<summary><b>🌐 Autodidactas y Curiosos (Gratis)</b></summary>

Si encontraste este repositorio por tu cuenta:

- ✅ **Todo el contenido es gratuito** y de código abierto
- ✅ Puedes aprender **a tu ritmo** sin presión
- ✅ Practica con **ejercicios reales** de Big Data
- ⚠️ **No incluye soporte** (solo para alumnos presenciales)

**Ventaja:** Material profesional de calidad sin costo, perfecto para tu portafolio.

</details>

<details>
<summary><b>💼 Empresas y Profesionales</b></summary>

Si buscas soluciones para tu empresa:

- ✅ **Portfolio real** de capacidades en Big Data
- ✅ Muestra cómo **entreno equipos** profesionales
- ✅ **Consultoría y capacitación** in-company disponible
- ✅ Proyectos de **análisis de datos a medida**

**Ventaja:** Ve exactamente qué nivel de calidad ofrezco antes de contratarme.

</details>

---

## 🎓 ¿Qué Aprenderás?

### Roadmap de Aprendizaje

```
┌─────────────────────────────────────────────────────────────┐
│                    TU VIAJE EN BIG DATA                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  NIVEL 1: Fundamentos                                       │
│  ├─ SQLite: Bases de datos relacionales                    │
│  ├─ Pandas: Análisis de datos en memoria                   │
│  └─ Git/GitHub: Control de versiones                       │
│                                                              │
│           ↓ Aprenderás en 2-3 semanas                      │
│                                                              │
│  NIVEL 2: Escalando                                         │
│  ├─ Dask: Procesamiento paralelo (datos > RAM)            │
│  ├─ Parquet: Almacenamiento columnar eficiente            │
│  └─ Optimización: Técnicas de performance                  │
│                                                              │
│           ↓ Aprenderás en 3-4 semanas                      │
│                                                              │
│  NIVEL 3: Big Data Real                                     │
│  ├─ PySpark: Procesamiento distribuido                     │
│  ├─ SQL avanzado: Queries complejas                        │
│  └─ Pipelines: ETL/ELT en producción                       │
│                                                              │
│           ↓ Aprenderás en 4-5 semanas                      │
│                                                              │
│  NIVEL 4: Visualización y Deploy                            │
│  ├─ Dashboards: Flask + Chart.js                           │
│  ├─ APIs: Servir datos procesados                          │
│  └─ Deploy: Poner en producción                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘

⏱️ Tiempo total estimado: 10-12 semanas (a tu ritmo)
```

### Tecnologías que Dominarás

| Tecnología | Qué Hace | Cuándo Usarla |
|------------|----------|---------------|
| **Python** | Lenguaje base | Siempre |
| **Pandas** | Datos en memoria (< 5GB) | Análisis exploratorio |
| **Dask** | Datos > RAM (5-100GB) | Datasets grandes en 1 máquina |
| **PySpark** | Datos masivos (> 100GB) | Clusters, producción |
| **SQLite** | Base de datos embebida | Prototipos, proyectos pequeños |
| **Parquet** | Formato columnar | Almacenar datos procesados |
| **Git/GitHub** | Control de versiones | Todo proyecto profesional |
| **Flask** | Web framework | Dashboards, APIs |

### Ejemplos de Qué Podrás Hacer

**Ejemplo 1: Analizar 10 Millones de Viajes de Taxi**

```python
# Dataset: NYC Taxi (121 MB CSV, 10M+ registros)
# Pregunta: ¿Cuál es el ingreso promedio por hora del día?

import dask.dataframe as dd

# Cargar 121 MB como si fueran 10 MB ⚡
df = dd.read_csv("yellow_tripdata_2021-01.csv")

# Análisis que en Pandas tomaría 5 minutos, aquí: 10 segundos
resultado = (df.groupby(df['tpep_pickup_datetime'].dt.hour)
              ['total_amount']
              .mean()
              .compute())

print(resultado)
# Resultado: Hora 23 es la más rentable ($18.50 promedio)
```

**Ejemplo 2: Dashboard en Tiempo Real**

Crear un dashboard interactivo que muestra:
- 📊 Distribución de viajes por hora
- 🗺️ Mapa de calor de zonas más rentables
- 💰 Ingresos totales por día/semana/mes
- 📈 Tendencias temporales

**Ejemplo 3: Pipeline ETL de Producción**

```
CSV (100GB) → Limpiar → Transformar → Parquet → Dashboard
              (Dask)    (PySpark)    (10GB)     (Flask)
```

---

## 🚀 Cómo Empezar (Todos los Niveles)

### NIVEL 0: Primera Vez con Git y Python

<details>
<summary><b>Click aquí si es tu primera vez</b></summary>

#### Paso 1: Instalar Herramientas Básicas

**Windows:**
```bash
# Instalar Git
winget install Git.Git

# Instalar Python
winget install Python.Python.3.11

# Verificar instalación
git --version
python --version
```

**Mac:**
```bash
# Instalar Homebrew (si no lo tienes)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Git y Python
brew install git python@3.11

# Verificar
git --version
python3 --version
```

**Linux:**
```bash
sudo apt-get update
sudo apt-get install git python3.11 python3-pip
```

#### Paso 2: Configurar Git

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

#### Paso 3: Crear Cuenta en GitHub

1. Ir a https://github.com/
2. Click "Sign Up"
3. Verificar email

¡Listo! Ahora ve a **NIVEL 1** ↓

</details>

---

### NIVEL 1: Tengo Git y GitHub, ¿Ahora Qué?

<details>
<summary><b>Click aquí para el flujo completo</b></summary>

## 📋 FLUJO COMPLETO DE TRABAJO

### Visión General del Flujo

```
┌──────────────────────────────────────────────────────────────┐
│              FLUJO DE TRABAJO COMPLETO                       │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1. FORK                                                      │
│     ┌────────────────────────────────────┐                  │
│     │  Repositorio del Profesor (Origen)  │                  │
│     │  TodoEconometria/ejercicios-bigdata │                  │
│     └────────────────────────────────────┘                  │
│                    │                                          │
│                    │ Hacer Fork                               │
│                    ↓                                          │
│     ┌────────────────────────────────────┐                  │
│     │   TU Repositorio (Fork Público)     │                  │
│     │   TU_USUARIO/ejercicios-bigdata     │                  │
│     └────────────────────────────────────┘                  │
│                                                               │
│  2. CLONE                                                     │
│     git clone https://github.com/TU_USUARIO/...             │
│                    │                                          │
│                    ↓                                          │
│     ┌────────────────────────────────────┐                  │
│     │    Repositorio Local (Tu PC)        │                  │
│     │    ejercicios-bigdata/              │                  │
│     └────────────────────────────────────┘                  │
│                                                               │
│  3. CREAR REPO PRIVADO DE PRUEBAS (Opcional pero recomendado)│
│     ┌────────────────────────────────────┐                  │
│     │   TU Repo Privado (Experimentos)    │                  │
│     │   TU_USUARIO/bigdata-practica       │                  │
│     └────────────────────────────────────┘                  │
│                                                               │
│  4. TRABAJAR EN EJERCICIOS                                   │
│     - Editar código localmente                               │
│     - Hacer commits frecuentes                               │
│     - Probar en tu repo privado primero                      │
│                                                               │
│  5. PULL REQUEST (Entregar)                                  │
│     TU Fork → Repositorio del Profesor                       │
│                                                               │
│  6. FEEDBACK                                                 │
│     Profesor revisa → Comentarios → Correcciones            │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### PASO 1: Hacer Fork del Repositorio

**¿Qué es un Fork?**

Un fork es TU COPIA PERSONAL del repositorio. Piénsalo como fotocopiar un libro: el original sigue siendo del autor, pero tú puedes escribir en tu copia.

**Cómo hacer Fork:**

1. **Ir al repositorio original:**
   https://github.com/TodoEconometria/ejercicios-bigdata

2. **Click en "Fork"** (botón arriba a la derecha)

3. **Seleccionar tu cuenta** como destino

4. **¡Listo!** Ahora tienes tu propia copia en:
   `https://github.com/TU_USUARIO/ejercicios-bigdata`

**⚠️ IMPORTANTE:** Siempre trabaja en TU fork, NO en el repositorio original.

---

### PASO 2: Clonar TU Fork a Tu Computadora

```bash
# ❌ MAL - No clones el original
git clone https://github.com/TodoEconometria/ejercicios-bigdata.git

# ✅ BIEN - Clona TU fork
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# Entrar al directorio
cd ejercicios-bigdata

# Configurar el repositorio original como "upstream"
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git

# Verificar remotos
git remote -v
# Deberías ver:
# origin    → tu fork
# upstream  → repositorio original
```

---

### PASO 3: Crear Tu Repositorio Privado de Pruebas

#### ¿Por Qué Necesitas un Repo Privado?

**Historia real de lo que nos pasó:**

> *"Estaba desarrollando un ejercicio nuevo. Subí el borrador al repositorio público sin darme cuenta. Los alumnos vieron las soluciones antes de tiempo. Tuve que hacer rollback de emergencia y limpiar el historial de Git. Perdí 3 horas arreglando el desastre."*
> — Experiencia real del profesor

**Lecciones aprendidas:**

1. ❌ **Nunca experimentes directamente en el repositorio público**
2. ✅ **Siempre prueba primero en un repo privado**
3. ✅ **Solo publica cuando estés 100% seguro**

#### Opción A: Repositorio Privado Tradicional

**Crear repo privado:**

```bash
# 1. Ir a https://github.com/new

# 2. Configurar:
#    - Repository name: bigdata-practica (o como quieras)
#    - Description: "Mi espacio de práctica para Big Data"
#    - Visibility: 🔒 Private (MUY IMPORTANTE)
#    - Initialize: NO (dejar vacío)

# 3. Crear repositorio

# 4. En tu computadora, crear carpeta separada:
mkdir ../bigdata-practica
cd ../bigdata-practica

# 5. Inicializar y conectar
git init
git remote add origin https://github.com/TU_USUARIO/bigdata-practica.git

# 6. Copiar ejercicios para experimentar
cp -r ../ejercicios-bigdata/ejercicios/ .
cp -r ../ejercicios-bigdata/datos/ .

# 7. Hacer primer commit
git add .
git commit -m "Setup inicial de práctica"
git push -u origin main
```

**Flujo de trabajo con repo privado:**

```
ejercicios-bigdata/          ← Fork público (entregas)
│
└─ ejercicios/
   └─ 01_cargar_sqlite.py

bigdata-practica/            ← Repo privado (experimentos)
│
├─ prueba_01.py             ← Experimentas aquí
├─ prueba_02_error.py       ← Si falla, no importa
└─ 01_solucion_final.py     ← Cuando funciona, copias al público
```

#### Opción B: GitHub Codespaces (Más Fácil)

**¿Qué es Codespaces?**

Un entorno de desarrollo completo en la nube. Como tener Visual Studio Code en tu navegador.

**Ventajas:**

- ✅ No necesitas instalar nada
- ✅ Funciona desde cualquier computadora
- ✅ Entorno aislado para experimentar
- ✅ 60 horas gratis al mes

**Cómo usar:**

1. En tu fork de GitHub, click en "Code" → "Codespaces" → "Create codespace"

2. Se abre VS Code en el navegador ✨

3. Terminal integrada para ejecutar código

4. Experimenta sin miedo - es tu espacio privado

5. Cuando estés listo, haz commit y push

**Recomendación:** Usa Codespaces para experimentos rápidos, repo privado para proyectos serios.

---

### PASO 4: Trabajar en un Ejercicio

#### Workflow Completo

```bash
# ═══════════════════════════════════════════════════════
# CADA VEZ QUE EMPIECES UN EJERCICIO NUEVO
# ═══════════════════════════════════════════════════════

# 1. Actualizar tu fork con cambios del profesor
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# 2. Crear una rama para el ejercicio (OPCIONAL pero recomendado)
git checkout -b ejercicio-01

# 3. Ir a la carpeta del ejercicio
cd ejercicios/01_cargar_sqlite.py

# 4. Leer el enunciado COMPLETO
cat ENUNCIADO.md  # Si existe
# O ver comentarios en el archivo .py

# 5. Experimentar primero en tu repo privado (si es complejo)
#    Copiar el archivo a bigdata-practica/
#    Probar diferentes enfoques
#    Cuando funcione, volver al repo público

# 6. Trabajar en el ejercicio
code 01_cargar_sqlite.py  # O tu editor favorito

# 7. Ejecutar y probar
python 01_cargar_sqlite.py

# 8. Si funciona, hacer commit
git add 01_cargar_sqlite.py
git commit -m "Ejercicio 01: Implementar carga de datos SQLite"

# 9. Si no funciona, seguir iterando
#    NO hagas commit de código roto

# 10. Cuando esté listo, subir a tu fork
git push origin ejercicio-01  # O main si no creaste rama
```

#### Tips para Resolver Ejercicios

**🎯 Antes de Empezar:**

```
□ Leí el enunciado COMPLETO (no solo el título)
□ Entendí QUÉ se pide (no cómo hacerlo todavía)
□ Identifiqué los datos de entrada y salida esperada
□ Busqué si hay un archivo AYUDA.md con pistas
```

**💻 Mientras Trabajo:**

```python
# ✅ BIEN - Desarrolla en pasos pequeños
# Paso 1: Cargar datos
df = pd.read_csv("datos.csv")
print(df.head())  # Verificar que cargó bien

# Paso 2: Limpiar datos
df = df.dropna()
print(f"Filas después de limpiar: {len(df)}")

# Paso 3: Analizar
resultado = df.groupby("categoria").sum()
print(resultado)

# ❌ MAL - Escribir todo de golpe
df = pd.read_csv("datos.csv").dropna().groupby("categoria").sum()
# Si falla, no sabes en qué paso fue el error
```

**🧪 Probar Frecuentemente:**

```bash
# No esperes a terminar todo para probar
python mi_ejercicio.py  # Ejecuta después de cada cambio importante
```

**📝 Commits Frecuentes:**

```bash
# ✅ BIEN
git commit -m "Ejercicio 01: Agregar función de carga"
git commit -m "Ejercicio 01: Implementar limpieza de nulos"
git commit -m "Ejercicio 01: Agregar análisis estadístico"

# ❌ MAL
git commit -m "ejercicio terminado"  # Vago, sin contexto
```

---

### PASO 5: Hacer Pull Request (Entregar)

#### ¿Qué es un Pull Request (PR)?

Un Pull Request es decir: *"Profe, terminé el ejercicio. ¿Puedes revisarlo?"*

Es como entregar una tarea, pero con superpoderes:
- El profesor ve exactamente QUÉ cambiaste
- Puede comentar líneas específicas de código
- Puedes hacer correcciones después
- Queda registro de todo el proceso

#### Cómo Crear un PR

**1. Asegúrate de que tu código funciona:**

```bash
# Ejecuta el ejercicio una última vez
python ejercicios/01_cargar_sqlite.py

# Revisa que no hay errores
# Verifica que cumple los requisitos del enunciado
```

**2. Sube tus cambios a tu fork:**

```bash
git push origin ejercicio-01  # O main si trabajaste ahí
```

**3. Ir a GitHub:**

Opción A: GitHub te muestra un banner amarillo automáticamente:
```
"ejercicio-01 had recent pushes"
[Compare & pull request]  ← Click aquí
```

Opción B: Manual:
1. Ir a tu fork: `https://github.com/TU_USUARIO/ejercicios-bigdata`
2. Click en "Pull requests" → "New pull request"
3. Seleccionar:
   - Base repository: `TodoEconometria/ejercicios-bigdata` (base: `main`)
   - Head repository: `TU_USUARIO/ejercicios-bigdata` (compare: `ejercicio-01`)

**4. Completar información del PR:**

```markdown
Título: Entrega Ejercicio 01: Carga de Datos SQLite - [Tu Nombre]

Descripción:
## ✅ Ejercicio Completado
Ejercicio 01: Análisis de datos con SQLite

## 📝 Qué Hice
- Implementé función para cargar datos desde CSV a SQLite
- Agregué validación de tipos de datos
- Creé queries SQL para análisis básico
- Generé reporte de estadísticas descriptivas

## 🧪 Pruebas Realizadas
- ✅ Probado con dataset de 10,000 registros
- ✅ Probado con datos con valores nulos
- ✅ Verificado que queries devuelven resultados esperados

## ⏱️ Tiempo Invertido
Aproximadamente 4 horas (incluyendo investigación)

## 🤔 Dificultades Encontradas
- Tuve problemas inicialmente con la codificación UTF-8 del CSV
- Solucionado agregando `encoding='utf-8'` en read_csv()

## 💡 Aprendizajes
- Aprendí la diferencia entre SQLite y bases de datos cliente-servidor
- Entendí cuándo usar índices en SQLite
- Practiqué optimización de queries

## 📚 Recursos Consultados
- Documentación oficial de SQLite
- Pandas documentation sobre to_sql()
- Stack Overflow para el problema de encoding

## 🙋 Preguntas para el Profesor
- ¿Hay una forma más eficiente de hacer bulk insert en SQLite?
- ¿Debería usar transactions para mejorar performance?
```

**5. Click "Create pull request"**

**6. Esperar revisión del profesor**

#### Después de Crear el PR

**Si el profesor pide cambios:**

```bash
# 1. Hacer las correcciones en tu código local
# Edita los archivos según los comentarios

# 2. Commitear los cambios
git add .
git commit -m "Correcciones según feedback: optimizar queries"

# 3. Subir cambios
git push origin ejercicio-01

# 4. El PR se actualiza automáticamente ✨
# No necesitas crear un nuevo PR
```

**Si el profesor aprueba:**

🎉 ¡Felicitaciones! Tu código fue aceptado.

---

### PASO 6: Mantener tu Fork Actualizado

El profesor subirá nuevos ejercicios y actualizaciones. Necesitas sincronizar:

```bash
# Hacer esto SEMANALMENTE o antes de empezar un nuevo ejercicio

# 1. Cambiar a main
git checkout main

# 2. Descargar cambios del profesor
git fetch upstream

# 3. Integrar cambios
git merge upstream/main

# Si hay conflictos (raro), Git te avisará
# Resuelve manualmente y haz commit

# 4. Subir actualizaciones a tu fork
git push origin main

# ¡Listo! Tu fork está actualizado
```

---

</details>

---

### NIVEL 2: Soy Desarrollador, Dame lo Esencial

<details>
<summary><b>TL;DR para devs experimentados</b></summary>

```bash
# Setup (1 minuto)
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Workflow
git fetch upstream && git merge upstream/main
git checkout -b ejercicio-XX
# ... work ...
git push origin ejercicio-XX
# Create PR on GitHub

# Actualizar
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

**Estructura del repo:**
```
ejercicios-bigdata/
├── ejercicios/          # Ejercicios progresivos
├── datos/               # Datasets (NYC Taxi, etc.)
├── dashboards/          # Ejemplos de viz
└── docs/                # Guías adicionales
```

**Tech stack:**
- Python 3.11+
- Pandas, Dask, PySpark
- SQLite, Parquet
- Flask para dashboards

</details>

---

## 📚 Ejercicios Disponibles

### Roadmap Detallado

| # | Ejercicio | Tecnología | Nivel | Tiempo Estimado |
|---|-----------|------------|-------|-----------------|
| 01 | Carga de Datos con SQLite | SQLite + Pandas | 🟢 Básico | 2-3 horas |
| 02 | Limpieza y Transformación | Pandas | 🟢 Básico | 3-4 horas |
| 03 | Procesamiento con Parquet y Dask | Dask + Parquet | 🟡 Intermedio | 4-5 horas |
| 04 | Queries Complejas con PySpark | PySpark | 🟡 Intermedio | 5-6 horas |
| 05 | Dashboard Interactivo | Flask + Chart.js | 🔴 Avanzado | 8-10 horas |
| 06 | Pipeline ETL Completo | Dask + PySpark | 🔴 Avanzado | 10-12 horas |

### Ejercicio 01: Carga de Datos con SQLite

**¿Qué aprenderás?**
- Cargar datos desde CSV a base de datos
- Queries SQL básicas (SELECT, WHERE, GROUP BY)
- Optimización con índices
- Exportar resultados

**Dataset:** NYC Taxi Trips (121 MB, 10M+ registros)

**Desafío:** Cargar y analizar datos de taxis sin que tu computadora se congele.

<details>
<summary><b>Ver ejemplo de solución</b></summary>

```python
import sqlite3
import pandas as pd

# Cargar CSV en chunks (por partes)
chunksize = 100000
chunks = pd.read_csv("yellow_tripdata_2021-01.csv", chunksize=chunksize)

# Crear base de datos SQLite
conn = sqlite3.connect("taxi.db")

# Cargar por chunks
for i, chunk in enumerate(chunks):
    chunk.to_sql("trips", conn, if_exists="append", index=False)
    print(f"Chunk {i+1} cargado ({len(chunk)} registros)")

# Crear índices para acelerar queries
conn.execute("CREATE INDEX idx_pickup ON trips(tpep_pickup_datetime)")

# Query ejemplo: Promedio de tarifa por hora
query = """
    SELECT
        strftime('%H', tpep_pickup_datetime) as hora,
        AVG(total_amount) as promedio_tarifa,
        COUNT(*) as num_viajes
    FROM trips
    GROUP BY hora
    ORDER BY hora
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)

conn.close()
```

**Output esperado:**
```
hora  promedio_tarifa  num_viajes
00    15.23           234567
01    14.89           198234
02    16.45           165789
...
```

</details>

---

### Ejercicio 02: Limpieza y Transformación

**¿Qué aprenderás?**
- Detectar y manejar valores nulos
- Identificar outliers
- Transformaciones de datos
- Validación de tipos

**Dataset:** Mismo NYC Taxi (pero "sucio")

**Desafío:** Datos del mundo real siempre vienen sucios. Aprender a limpiarlos profesionalmente.

---

### Ejercicio 03: Procesamiento con Parquet y Dask

**¿Qué aprenderás?**
- Por qué Parquet es mejor que CSV
- Procesamiento paralelo con Dask
- Lazy evaluation
- Optimización de memoria

**Dataset:** NYC Taxi (convertido a Parquet)

**Desafío:** Procesar 10GB de datos en una laptop de 8GB RAM.

---

### Ejercicio 04: Queries Complejas con PySpark

**¿Qué aprenderás?**
- Introducción a Spark
- DataFrames distribuidos
- SQL en Spark
- Particionamiento de datos

**Dataset:** NYC Taxi + Weather Data (join de múltiples fuentes)

**Desafío:** Combinar datos de diferentes fuentes y hacer análisis complejos.

---

### Ejercicio 05: Dashboard Interactivo

**¿Qué aprenderás?**
- Flask para backend
- Chart.js para visualizaciones
- Conectar frontend con análisis de datos
- Deploy local

**Proyecto:** Dashboard EDA (Exploratory Data Analysis) de NYC Taxi

**Desafío:** Crear un dashboard profesional que impresione en entrevistas.

---

## 🔧 Setup del Entorno de Desarrollo

### Instalación de Dependencias

```bash
# Clonar el repositorio (tu fork)
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
python -c "import pandas, dask, pyspark; print('Todo OK!')"
```

### Estructura de Carpetas

```
ejercicios-bigdata/
│
├── .github/                    # Templates de issues y PRs
├── datos/                      # Datasets
│   ├── README.md              # Cómo descargar datos
│   └── descargar_datos.py     # Script automático
│
├── ejercicios/                 # Ejercicios del curso
│   ├── 01_cargar_sqlite.py
│   ├── 02_limpieza_datos.py
│   ├── 03_parquet_dask.py
│   ├── 04_pyspark_query.py
│   └── [futuros ejercicios]
│
├── dashboards/                 # Ejemplos de visualización
│   ├── nyc_taxi_eda/          # Dashboard ejemplo
│   └── ejemplos-destacados/   # Galería de proyectos
│
├── docs/                       # Documentación adicional
│   ├── CONFIGURACION_INICIAL.md
│   ├── GUIA_ENTREGA_DASHBOARDS.md
│   └── INSTRUCCIONES_ALUMNOS.md
│
├── .gitignore                  # Archivos ignorados por Git
├── requirements.txt            # Dependencias Python
├── PARA_ALUMNOS.md            # Info específica del curso
└── README.md                   # Este archivo
```

---

## 🌟 Ejemplos Destacados

### Dashboard NYC Taxi EDA

![Dashboard Preview](dashboards/nyc_taxi_eda/preview.png)

**Características:**
- Visualización interactiva de 10M+ registros
- Filtros dinámicos por fecha, hora, zona
- Mapas de calor de rutas más rentables
- Análisis de tendencias temporales

**Tecnologías:**
- Backend: Flask + Pandas
- Frontend: Chart.js + Leaflet.js
- Deploy: Docker

**Ver código:** [`dashboards/nyc_taxi_eda/`](dashboards/nyc_taxi_eda/)

---

## ❓ Preguntas Frecuentes (FAQ)

<details>
<summary><b>¿Necesito experiencia previa en Big Data?</b></summary>

**No.** El curso empieza desde cero. Solo necesitas:
- Conocimientos básicos de Python
- Saber usar la terminal/consola
- Ganas de aprender

Si no tienes experiencia con Python, te recomiendo hacer estos tutoriales primero:
- [Learn Python (Codecademy)](https://www.codecademy.com/learn/learn-python-3)
- [Python for Everybody (Coursera)](https://www.coursera.org/specializations/python)

</details>

<details>
<summary><b>¿Cuánto tiempo toma completar los ejercicios?</b></summary>

**Depende de tu nivel:**

- **Principiantes:** 10-12 semanas (10-15 horas/semana)
- **Intermedios:** 6-8 semanas (8-10 horas/semana)
- **Avanzados:** 4-5 semanas (5-8 horas/semana)

No hay prisa. Aprende a tu ritmo.

</details>

<details>
<summary><b>¿Los datos son reales o sintéticos?</b></summary>

**Reales.** Usamos datasets públicos reales:
- NYC Taxi & Limousine Commission (TLC)
- Weather data de NOAA
- Otros datasets públicos de Kaggle

Esto te da experiencia con datos del mundo real (sucios, incompletos, grandes).

</details>

<details>
<summary><b>¿Puedo usar esto en mi portafolio?</b></summary>

**¡SÍ!** De hecho, te lo recomiendo.

Muchos alumnos han conseguido trabajo mostrando:
- Sus soluciones de los ejercicios
- El dashboard que crearon
- Su fork de GitHub con commits profesionales

Tip: Haz tu fork público y agrega un README personalizado explicando tu aprendizaje.

</details>

<details>
<summary><b>¿Hay certificado al terminar?</b></summary>

**Para alumnos del curso presencial:** Sí, certificado de 230 horas.

**Para autodidactas:** No hay certificado oficial, pero tu GitHub es tu certificado. Los empleadores valoran más ver tu código que un PDF.

</details>

<details>
<summary><b>¿Qué computadora necesito?</b></summary>

**Mínimo:**
- 8GB RAM
- 20GB espacio en disco
- Procesador i5 o equivalente

**Recomendado:**
- 16GB RAM
- 50GB espacio en disco SSD
- Procesador i7 o equivalente

**Nota:** Si tienes menos recursos, puedes usar Google Colab o GitHub Codespaces (gratis).

</details>

<details>
<summary><b>¿Ofrecen soporte si me atoró?</b></summary>

**Para alumnos del curso presencial:** Sí, soporte completo en las sesiones.

**Para autodidactas:** No hay soporte directo, pero puedes:
- Crear un Issue en GitHub con tu pregunta
- Buscar en Issues existentes (probablemente alguien más tuvo tu problema)
- Unirte a la comunidad de Python/Data Science en Discord/Slack

</details>

---

## 💼 Servicios Profesionales

### Consultoría en Big Data

¿Necesitas ayuda con un proyecto de datos en tu empresa?

**Ofrezco:**

- ✅ **Desarrollo de Pipelines ETL/ELT** con Python y Spark
- ✅ **Capacitación Empresarial** (cursos personalizados para tu equipo)
- ✅ **Análisis de Datos** para insights accionables
- ✅ **Automatización de Procesos** de datos
- ✅ **Migración a Big Data** (de Excel/SQL a Dask/Spark)

**Casos de uso:**

```
Empresa A: "Tenemos 5 años de ventas en Excel y toma 2 horas generar reportes"
→ Solución: Pipeline automatizado con Dask + Dashboard en tiempo real
→ Resultado: Reportes en 30 segundos

Empresa B: "Queremos capacitar a 15 analistas en Big Data"
→ Solución: Curso in-company de 40 horas adaptado a su industria
→ Resultado: Equipo autónomo procesando TB de datos

Startup C: "Necesitamos procesar logs de servidores (1TB/día)"
→ Solución: Pipeline PySpark en AWS EMR
→ Resultado: Análisis en tiempo real con costos optimizados
```

### Capacitación Empresarial

Entreno equipos en:

- **Nivel Básico:** Fundamentos de Python para Datos (40 horas)
- **Nivel Intermedio:** Pandas y Análisis Exploratorio (60 horas)
- **Nivel Avanzado:** Big Data con Dask y PySpark (80 horas)
- **Personalizado:** Adaptado a tu industria y tecnologías

**Modalidades:**
- Presencial (CDMX y área metropolitana)
- Online (Zoom/Teams)
- Híbrido

### Contacto

📧 **Email:** [cursos@todoeconometria.com](mailto:cursos@todoeconometria.com)
💼 **LinkedIn:** [Juan Gutierrez](https://www.linkedin.com/in/juangutierrezconsultor/)
🌐 **Web:** [www.todoeconometria.com](https://www.todoeconometria.com)

<!-- Sección lista pero oculta hasta que esté la infraestructura web
### 💰 Inversión

**Consultoría:**
- Sesión de 1 hora: [Precio]
- Paquete 5 horas: [Precio] (ahorras X%)
- Proyecto completo: Cotización personalizada

**Capacitación:**
- Curso básico (40h): [Precio]
- Curso intermedio (60h): [Precio]
- Curso avanzado (80h): [Precio]
- Descuento por grupos: 3+ personas, 15% off

📅 **Agendar reunión:** [Calendly link]
-->

---

## 🤝 Contribuciones

Este repositorio está en constante evolución. Si encuentras:
- 🐛 Errores o bugs
- 📝 Mejoras en la documentación
- 💡 Ideas para nuevos ejercicios
- 🎨 Ejemplos de dashboards

**Crea un Issue o Pull Request:**

1. Fork este repositorio
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

**En resumen:** Puedes usar este material para aprender, enseñar, o modificar, siempre que des crédito.

---

## 🙏 Agradecimientos

Este repositorio existe gracias a:

- **Mis alumnos** - Cuyas preguntas y feedback mejoran el contenido constantemente
- **NYC Open Data** - Por los datasets públicos
- **Comunidad de Python** - Pandas, Dask, PySpark developers
- **GitHub** - Por la plataforma que facilita el aprendizaje colaborativo

---

## 📊 Estadísticas del Repositorio

![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)
![GitHub forks](https://img.shields.io/github/forks/TodoEconometria/ejercicios-bigdata?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/TodoEconometria/ejercicios-bigdata?style=social)

---

## 🚀 ¿Listo para Empezar?

```bash
# 1. Haz fork de este repositorio (botón arriba a la derecha)

# 2. Clona TU fork
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# 3. Instala dependencias
cd ejercicios-bigdata
pip install -r requirements.txt

# 4. Empieza con el Ejercicio 01
cd ejercicios
python 01_cargar_sqlite.py

# 5. ¡Aprende, practica, crece! 🎓
```

---

<p align="center">
  <b>Tu carrera en Big Data empieza aquí.</b><br>
  ¿Preguntas? Abre un <a href="../../issues">Issue</a> o contáctame en <a href="https://www.linkedin.com/in/juangutierrezconsultor/">LinkedIn</a>
</p>

<p align="center">
  Hecho con ❤️ por <a href="https://www.todoeconometria.com">TodoEconometria</a>
</p>
