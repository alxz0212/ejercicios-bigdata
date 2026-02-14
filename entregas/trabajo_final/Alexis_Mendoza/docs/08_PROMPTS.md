# Registro de Prompts - Trabajo Final

**Alumno:** Daniel Alexis Mendoza Corne
**Fecha:** Febrero 2026
**IA utilizada:** Gemini

---

## COMO USAR ESTE ARCHIVO

Este archivo tiene **DOS PARTES** muy diferentes:

| Parte | Que es | Como debe verse |
|-------|--------|-----------------|
| **PARTE 1** | Tus 3 prompts reales | Lenguaje NATURAL, con errores, informal |
| **PARTE 2** | Blueprint generado por IA | Perfecto, profesional, estructurado |

### REGLA IMPORTANTE

> **Los prompts de la Parte 1 deben ser COPIA EXACTA de lo que escribiste.**
>
> NO los pases por la IA para "mejorarlos". NO corrijas errores.
> Si escribiste "como ago para que sparck lea el csv" con errores,
> eso es lo que debes pegar.
>
> **El sistema detecta automaticamente si los prompts fueron "limpiados".**
> Prompts perfectos en la Parte 1 = SOSPECHOSO.

---

# PARTE 1: Mis Prompts Reales (3 minimo)

> Copia y pega EXACTAMENTE lo que le escribiste a la IA.
> Incluye errores, lenguaje informal, todo. Eso demuestra autenticidad.

---

## Prompt A: Infraestructura Docker

**Contexto:** Necesitaba configurar un entorno con Jupyter, Spark y Base de datos, pero el script tenía problemas.

**Mi prompt exacto (copiado tal cual):**
```
quiero automatizar el script de setup spark para que corra con un comando y detecte el drive correcto sin que yo meta inputs
```

**Que paso:** [x] Funciono  [ ] Funciono parcial  [ ] No funciono

**Que aprendi:** Que Docker Compose y scripts batch pueden combinarse para simplificar enormemente el despliegue de infraestructura compleja en Windows.

---

## Prompt B: Pipeline ETL / Spark

**Contexto:** Estaba teniendo problemas con la visualización de datos en Dash y decidí cambiar a Streamlit.

**Mi prompt exacto (copiado tal cual):**
```
mis graficos en dash salen en blanco y no cargan, ayuda para migrar esto a streamlit porque dash me esta dando muchos problemas de renderizado
```

**Que paso:** [x] Funciono  [ ] Funciono parcial  [ ] No funciono

**Que aprendi:** Streamlit es mucho más directo para prototipado rápido de datos que Dash, aunque Dash ofrece más control fino sobre el layout.

---

## Prompt C: Analisis / Graficos

**Contexto:** Quería añadir un análisis más profundo y profesional al proyecto, validando el modelo econométrico.

**Mi prompt exacto (copiado tal cual):**
```
agregame un analisis econometrico tipo hausman para validar si el modelo de efectos fijos es mejor que el aleatorio en python
```

**Que paso:** [x] Funciono  [ ] Funciono parcial  [ ] No funciono

**Que aprendi:** Cómo integrar bibliotecas estadísticas como `statsmodels` dentro de un flujo de trabajo de Big Data para validación rigurosa.

---

# PARTE 2: Blueprint Replicable (generado por IA)

> **Instrucciones:** Cuando termines tu proyecto, pidele a tu IA:
>
> *"Genera un prompt profesional tipo blueprint que describa exactamente
> lo que logramos: stack, tecnologias, arquitectura, datos y pasos.
> Debe ser tan detallado que si se lo paso a otra IA o a un desarrollador
> senior, pueda replicar el proyecto completo sin ver mi codigo."*
>
> Pega la respuesta completa aqui abajo.

---

## Mi Blueprint

**Prompt que use para generar esto:**
```
Genera un prompt profesional tipo blueprint que describa exactamente lo que logramos: stack, tecnologias, arquitectura, datos y pasos. Debe ser tan detallado que si se lo paso a otra IA o a un desarrollador senior, pueda replicar el proyecto completo sin ver mi codigo.
```

**Blueprint generado por la IA:**

```
─────────────────────────────────────────────────────────────────
PROYECTO: Pipeline Big Data - Análisis de Calidad de Gobierno (QOG)

INFRAESTRUCTURA:
- Docker Compose orquestando 4 servicios principales:
  * PostgreSQL 13 (puerto 5432, persistencia en ./data/postgres)
  * Spark Master 3.5.1 (puertos 8081 UI, 7077 RPC)
  * Spark Worker (1GB RAM, 1 core, conectado a spark-master)
  * JupyterLab (Python 3.11, puertos 8888, 4040 SparkUI, 8501 Streamlit)
- Red: 'bigdata-net' (bridge)
- Volúmenes: Montaje local del directorio de trabajo en /home/jovyan/work

DATOS:
- Dataset Principal: Quality of Government (QOG) Standard Time-Series (qog_std_ts_jan26.csv)
- Fuente: Instituto de Calidad de Gobierno, Universidad de Gotemburgo
- Variables Clave: Índices de corrupción, estabilidad política, PIB per cápita, gasto en educación/salud.
- Periodo: Series temporales desde 1946 hasta la actualidad.

PIPELINE ETL (Python + PySpark):
1. Ingesta: Descarga automatizada del dataset QOG si no existe localmente (download_data.py).
2. Procesamiento: Lectura del CSV con PySpark, limpieza de nulos, casteo de tipos y filtrado de columnas relevantes.
3. Almacenamiento: Escritura de datos procesados en formato Parquet particionado para eficiencia.
4. Transformación: Agregaciones temporales y por país.

ANÁLISIS Y MODELADO:
- Análisis Exploratorio (EDA): Estadísticas descriptivas, distribución de variables.
- Machine Learning (Spark ML): Random Forest Regressor para predecir índices de estabilidad política basados en factores económicos.
- Econometría (Statsmodels): Test de Hausman para decidir entre Efectos Fijos (FE) y Aleatorios (RE) en datos de panel.

VISUALIZACIÓN (DASHBOARD):
- Herramienta: Streamlit
- Componentes:
  * Mapa coroplético interactivo (Plotly) de indicadores mundiales.
  * Gráficos de tendencias temporales (Line charts).
  * Matriz de correlación (Heatmap).
  * Sección de "Chat con tus Datos" (intefaz simulada de IA).

TECNOLOGÍAS:
- Python 3.11
- Apache Spark 3.5.1 (PySpark)
- PostgreSQL 13
- Docker & Docker Compose
- Bibliotecas Python: Streamlit, Plotly, Pandas, Scikit-learn, Statsmodels, Matplotlib, Seaborn.

COMANDO PARA EJECUTAR:
docker-compose up -d --build && docker exec jupyter_lab python src/pipeline.py && docker exec -d jupyter_lab streamlit run src/app_streamlit_pro.py
─────────────────────────────────────────────────────────────────
```

---

## Verificacion de Coherencia

Responde estas preguntas para verificar que tu blueprint coincide con tu codigo:

| Pregunta | Tu respuesta |
|----------|--------------|
| La version de Spark en el blueprint coincide con tu docker-compose.yml? | Si (3.5.1) |
| Los paises del blueprint son los mismos que filtra tu pipeline.py? | Si (Mundial/QOG std) |
| Las variables del blueprint estan en tu codigo? | Si |
| El tipo de analisis del blueprint coincide con tus graficos? | Si (Random Forest + Hausman) |

**Si alguna respuesta es "No", corrige el blueprint o el codigo.**

---

## Estadisticas Finales

| Metrica | Valor |
|---------|-------|
| Total de interacciones con IA (aprox) | 45 |
| Prompts que funcionaron a la primera | 30 |
| Errores que tuve que resolver | 10 |
| Horas totales de trabajo | 12 |

---

## Declaracion

[ ] Confirmo que los prompts de la PARTE 1 son reales y no fueron
    modificados ni pasados por IA para corregirlos.

[ ] Confirmo que el blueprint de la PARTE 2 fue generado por IA
    basandose en mi proyecto real.

[ ] Entiendo que inconsistencias entre el blueprint y mi codigo
    seran investigadas.

**Nombre:** Daniel Alexis Mendoza Corne
**Fecha:** Febrero 2026
