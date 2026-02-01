# Guia de Inicio Rapido: Tu Primer Pipeline de Datos

**Curso:** Big Data con Python
**Profesor:** Juan Marcelo Gutierrez Miranda (@TodoEconometria)
**Nivel:** Principiante - No se requiere experiencia previa en pipelines

---

## Que vas a construir

Un **pipeline de datos** es una cadena de pasos automatizados que transforma datos
crudos en informacion util. Al terminar esta guia tendras:

```
Datos crudos (CSV) --> Limpieza (ETL) --> Analisis --> Graficos --> Conclusiones
```

Usaras el dataset **Quality of Government (QoG)** de la Universidad de Gotemburgo,
que contiene indicadores de 194 paises desde 1946 hasta 2023: democracia, corrupcion,
PIB, salud, educacion, medio ambiente y mas.

---

## Paso 0: Preparar tu entorno

### Requisitos minimos

- Python 3.10 o superior
- Terminal (PowerShell en Windows, Terminal en Mac/Linux)
- Un editor de codigo (VSCode, PyCharm, o el que prefieras)

### Instalar dependencias

Desde la raiz del repositorio:

```powershell
pip install pandas numpy matplotlib seaborn scikit-learn pyarrow openpyxl
```

Si vas a usar PostgreSQL (opcional para empezar):

```powershell
pip install psycopg2-binary sqlalchemy
```

Si vas a usar Dask o Spark (nivel avanzado):

```powershell
pip install "dask[complete]"
pip install pyspark
```

---

## Paso 1: Descargar los datos

El dataset QoG es un CSV de aproximadamente 45 MB con ~15,000 filas y ~1,900 columnas.

### Opcion A: Script automatico (recomendado)

```powershell
python scripts/download_datasets.py --dataset qog
```

Esto descarga el archivo a `datos/qog/qog_std_ts_jan24.csv`.

### Opcion B: Descarga manual

1. Ve a https://www.qog.pol.gu.se/data/datadownloads/qogstandarddata
2. Descarga "QoG Standard Time-Series (CSV)"
3. Guarda el archivo en `datos/qog/qog_std_ts_jan24.csv`

### Verificar la descarga

```python
import pandas as pd

df = pd.read_csv("datos/qog/qog_std_ts_jan24.csv", low_memory=False)
print(f"Filas: {len(df):,}")
print(f"Columnas: {len(df.columns):,}")
print(f"Paises: {df['cname'].nunique()}")
print(f"Anios: {df['year'].min()} - {df['year'].max()}")
```

Resultado esperado: ~15,000 filas, ~1,900 columnas, 194 paises, 1946-2023.

---

## Paso 2: Elegir tu area de investigacion

No necesitas usar las 1,900 columnas. Elige **un area tematica** y trabaja con
5-10 variables relevantes. Aqui tienes opciones sugeridas:

### Area A: Democracia y gobernanza

Pregunta: Como ha cambiado la calidad democratica en diferentes regiones?

| Variable QoG | Que mide | Rango |
|---|---|---|
| `vdem_polyarchy` | Indice de democracia electoral (V-Dem) | 0-1 |
| `ti_cpi` | Corrupcion percibida (Transparency Intl) | 0-100 (100=limpio) |
| `p_polity2` | Regimen politico (Polity IV) | -10 a +10 |
| `fh_pr` | Derechos politicos (Freedom House) | 1-7 (1=mas libre) |
| `fh_cl` | Libertades civiles (Freedom House) | 1-7 (1=mas libre) |

### Area B: Desarrollo humano y economia

Pregunta: Que relacion hay entre riqueza economica y bienestar social?

| Variable QoG | Que mide | Unidad |
|---|---|---|
| `wdi_gdpcapcon2015` | PIB per capita (constantes 2015) | USD |
| `undp_hdi` | Indice de Desarrollo Humano | 0-1 |
| `wdi_lifexp` | Esperanza de vida al nacer | Anios |
| `wdi_litrat` | Tasa de alfabetizacion | % |
| `wdi_gini` | Desigualdad de ingresos (Gini) | 0-100 |

### Area C: Recursos naturales y medio ambiente

Pregunta: Los paises ricos en recursos naturales tienen mejor o peor gobernanza?

| Variable QoG | Que mide | Unidad |
|---|---|---|
| `wdi_resrent` | Rentas de recursos naturales | % del PIB |
| `ross_oil_value_pc2014` | Ingresos petroleo per capita | USD 2014 |
| `ross_gas_value_pc2014` | Ingresos gas per capita | USD 2014 |
| `wdi_agriland` | Tierra agricola | % del territorio |
| `wdi_co2` | Emisiones CO2 per capita | Toneladas |

### Area D: Seguridad y conflicto

Pregunta: Como se relacionan la estabilidad politica y el gasto militar?

| Variable QoG | Que mide | Rango |
|---|---|---|
| `wbgi_pve` | Estabilidad politica (World Bank) | -2.5 a +2.5 |
| `wdi_milit` | Gasto militar | % del PIB |
| `ffp_fsi` | Indice de fragilidad estatal | 0-120 (120=mas fragil) |
| `bti_ci` | Intensidad de conflicto (BTI) | 1-10 |

### Consejo: selecciona tambien paises

No analices 194 paises a la vez. Elige un grupo de 10-30 paises que tenga sentido
para tu pregunta. Ejemplos:

- **Union Europea (27):** Economias desarrolladas
- **America Latina (20):** Democracias en transicion
- **Asia Central (5):** Republicas post-sovieticas
- **BRICS (5):** Economias emergentes
- **Maghreb (5):** Norte de Africa

---

## Paso 3: Limpiar los datos (ETL)

Crea un archivo `etl.py` con la logica de limpieza:

```python
"""
ETL: Extraccion, Transformacion y Carga de datos QoG.
Adapta las variables y paises a tu area de investigacion.
"""
import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURACION - Modifica segun tu area elegida
# ============================================================
ARCHIVO_CSV = Path("datos/qog/qog_std_ts_jan24.csv")
ARCHIVO_SALIDA = Path("output/datos_limpios.parquet")

# Ejemplo: Area A - Democracia en America Latina
MIS_PAISES = [
    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia",
    "Costa Rica", "Cuba", "Dominican Republic", "Ecuador",
    "El Salvador", "Guatemala", "Honduras", "Mexico",
    "Nicaragua", "Panama", "Paraguay", "Peru", "Uruguay",
    "Venezuela"
]

MIS_VARIABLES = {
    # Identificadores (siempre incluir estos)
    "cname": "pais",
    "ccodealp": "codigo_pais",
    "year": "anio",
    # Variables de interes
    "vdem_polyarchy": "democracia",
    "ti_cpi": "corrupcion",
    "p_polity2": "regimen",
    "fh_pr": "derechos_politicos",
    "fh_cl": "libertades_civiles",
    # Contexto economico
    "wdi_gdpcapcon2015": "pib_percapita",
    "undp_hdi": "desarrollo_humano",
}

ANIO_INICIO = 1991
ANIO_FIN = 2023


# ============================================================
# FUNCIONES ETL
# ============================================================
def extraer(ruta_csv):
    """Lee el CSV crudo y selecciona columnas y filas relevantes."""
    print(f"Leyendo {ruta_csv.name} ...")
    df = pd.read_csv(str(ruta_csv), low_memory=False)
    print(f"  Dataset original: {len(df):,} filas x {len(df.columns):,} columnas")

    # Seleccionar solo las columnas que necesitamos
    columnas_disponibles = [c for c in MIS_VARIABLES.keys() if c in df.columns]
    df = df[columnas_disponibles].copy()

    # Filtrar paises
    df = df[df["cname"].isin(MIS_PAISES)]

    # Filtrar rango de anios
    df = df[(df["year"] >= ANIO_INICIO) & (df["year"] <= ANIO_FIN)]

    print(f"  Despues de filtrar: {len(df):,} filas x {len(df.columns)} columnas")
    return df


def transformar(df):
    """Limpia y transforma los datos."""
    # Renombrar columnas a nombres mas claros
    renombres = {k: v for k, v in MIS_VARIABLES.items() if k in df.columns}
    df = df.rename(columns=renombres)

    # Ordenar
    df = df.sort_values(["pais", "anio"]).reset_index(drop=True)

    # Mostrar estadisticas de valores nulos
    nulos = df.isnull().sum()
    nulos_pct = (nulos / len(df) * 100).round(1)
    print("\nValores nulos por columna:")
    for col in df.columns:
        if nulos[col] > 0:
            print(f"  {col}: {nulos[col]} ({nulos_pct[col]}%)")

    print(f"\nDataset limpio: {len(df):,} filas x {len(df.columns)} columnas")
    print(f"Paises: {df['pais'].nunique()}")
    print(f"Periodo: {df['anio'].min()} - {df['anio'].max()}")
    return df


def cargar(df, ruta_salida):
    """Guarda los datos limpios en formato Parquet."""
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(str(ruta_salida), index=False)
    tamano_kb = ruta_salida.stat().st_size / 1024
    print(f"\nGuardado en: {ruta_salida}")
    print(f"Tamano: {tamano_kb:.1f} KB")


# ============================================================
# EJECUCION
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  PIPELINE ETL - Quality of Government")
    print("=" * 50)

    df = extraer(ARCHIVO_CSV)
    df = transformar(df)
    cargar(df, ARCHIVO_SALIDA)

    print("\nETL completado.")
```

**Ejecutar:**

```powershell
python etl.py
```

---

## Paso 4: Analizar y visualizar

Crea un archivo `analisis.py`:

```python
"""
Analisis y visualizacion de datos QoG procesados.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Configuracion visual
sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams["figure.figsize"] = (12, 6)

ARCHIVO_DATOS = Path("output/datos_limpios.parquet")
CARPETA_FIGURAS = Path("output/figuras")
CARPETA_FIGURAS.mkdir(parents=True, exist_ok=True)


def cargar_datos():
    """Carga el Parquet generado por el ETL."""
    df = pd.read_parquet(str(ARCHIVO_DATOS))
    print(f"Datos cargados: {len(df):,} filas")
    return df


# ============================================================
# GRAFICO 1: Evolucion temporal de una variable
# ============================================================
def grafico_evolucion(df, variable, titulo):
    """Lineas temporales por pais."""
    fig, ax = plt.subplots(figsize=(14, 7))

    for pais in df["pais"].unique():
        datos_pais = df[df["pais"] == pais]
        ax.plot(datos_pais["anio"], datos_pais[variable],
                label=pais, linewidth=1.5, alpha=0.8)

    ax.set_xlabel("Anio")
    ax.set_ylabel(variable.replace("_", " ").title())
    ax.set_title(titulo)
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=8)
    plt.tight_layout()

    ruta = CARPETA_FIGURAS / f"evolucion_{variable}.png"
    fig.savefig(str(ruta), dpi=150, bbox_inches="tight")
    print(f"  Guardado: {ruta}")
    plt.close()


# ============================================================
# GRAFICO 2: Correlaciones entre variables
# ============================================================
def grafico_correlaciones(df, variables):
    """Matriz de correlacion."""
    corr = df[variables].corr()

    fig, ax = plt.subplots(figsize=(8, 7))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r",
                center=0, vmin=-1, vmax=1, ax=ax,
                square=True, linewidths=0.5)
    ax.set_title("Matriz de Correlaciones")
    plt.tight_layout()

    ruta = CARPETA_FIGURAS / "correlaciones.png"
    fig.savefig(str(ruta), dpi=150)
    print(f"  Guardado: {ruta}")
    plt.close()


# ============================================================
# GRAFICO 3: Comparacion de paises (ultimo anio disponible)
# ============================================================
def grafico_barras(df, variable, titulo):
    """Barras horizontales comparando paises."""
    # Tomar el ultimo anio con datos para cada pais
    ultimo = df.dropna(subset=[variable])
    ultimo = ultimo.sort_values("anio").groupby("pais").last().reset_index()
    ultimo = ultimo.sort_values(variable, ascending=True)

    fig, ax = plt.subplots(figsize=(10, max(6, len(ultimo) * 0.4)))
    colores = sns.color_palette("viridis", len(ultimo))
    ax.barh(ultimo["pais"], ultimo[variable], color=colores)
    ax.set_xlabel(variable.replace("_", " ").title())
    ax.set_title(titulo)
    plt.tight_layout()

    ruta = CARPETA_FIGURAS / f"barras_{variable}.png"
    fig.savefig(str(ruta), dpi=150, bbox_inches="tight")
    print(f"  Guardado: {ruta}")
    plt.close()


# ============================================================
# GRAFICO 4: Scatter - relacion entre dos variables
# ============================================================
def grafico_scatter(df, var_x, var_y, titulo):
    """Dispersion entre dos variables (ultimo anio)."""
    ultimo = df.dropna(subset=[var_x, var_y])
    ultimo = ultimo.sort_values("anio").groupby("pais").last().reset_index()

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(ultimo[var_x], ultimo[var_y], s=80, alpha=0.7, edgecolors="black")

    # Etiquetar cada punto con el nombre del pais
    for _, row in ultimo.iterrows():
        ax.annotate(row["codigo_pais"], (row[var_x], row[var_y]),
                     fontsize=7, ha="center", va="bottom")

    ax.set_xlabel(var_x.replace("_", " ").title())
    ax.set_ylabel(var_y.replace("_", " ").title())
    ax.set_title(titulo)
    plt.tight_layout()

    ruta = CARPETA_FIGURAS / f"scatter_{var_x}_vs_{var_y}.png"
    fig.savefig(str(ruta), dpi=150, bbox_inches="tight")
    print(f"  Guardado: {ruta}")
    plt.close()


# ============================================================
# EJECUCION
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  ANALISIS - Quality of Government")
    print("=" * 50)

    df = cargar_datos()

    print("\nGenerando graficos...")

    # Adapta estos a tus variables
    grafico_evolucion(df, "democracia",
                      "Evolucion de la Democracia en America Latina")

    grafico_evolucion(df, "pib_percapita",
                      "PIB per Capita en America Latina (USD 2015)")

    variables_numericas = [c for c in df.select_dtypes("number").columns
                           if c != "anio"]
    grafico_correlaciones(df, variables_numericas)

    grafico_barras(df, "democracia",
                   "Democracia por Pais (ultimo dato disponible)")

    grafico_scatter(df, "pib_percapita", "democracia",
                    "PIB per Capita vs Democracia")

    print(f"\nTodas las figuras guardadas en: {CARPETA_FIGURAS}/")
    print("Analisis completado.")
```

**Ejecutar:**

```powershell
python analisis.py
```

---

## Paso 5: Crear tu script principal

Crea `main.py` para orquestar todo el pipeline:

```python
"""
Pipeline principal: ejecuta ETL + Analisis en secuencia.
"""
import time

if __name__ == "__main__":
    inicio = time.time()

    print("=" * 50)
    print("  PIPELINE COMPLETO")
    print("=" * 50)

    # Paso 1: ETL
    print("\n--- Paso 1/2: ETL ---")
    from etl import extraer, transformar, cargar, ARCHIVO_CSV, ARCHIVO_SALIDA
    df = extraer(ARCHIVO_CSV)
    df = transformar(df)
    cargar(df, ARCHIVO_SALIDA)

    # Paso 2: Analisis
    print("\n--- Paso 2/2: Analisis ---")
    import analisis
    df = analisis.cargar_datos()
    print("\nGenerando graficos...")
    analisis.grafico_evolucion(df, "democracia",
                               "Evolucion de la Democracia")
    analisis.grafico_evolucion(df, "pib_percapita",
                               "PIB per Capita (USD 2015)")
    variables_numericas = [c for c in df.select_dtypes("number").columns
                           if c != "anio"]
    analisis.grafico_correlaciones(df, variables_numericas)
    analisis.grafico_barras(df, "democracia",
                            "Democracia por Pais")
    analisis.grafico_scatter(df, "pib_percapita", "democracia",
                             "PIB per Capita vs Democracia")

    duracion = time.time() - inicio
    print(f"\nPIPELINE COMPLETADO en {duracion:.1f} segundos")
```

---

## Paso 6: Verificar que todo funciona

Ejecuta el pipeline completo:

```powershell
python main.py
```

Deberia mostrar:

```
PIPELINE COMPLETO
--- Paso 1/2: ETL ---
Leyendo qog_std_ts_jan24.csv ...
  Dataset original: ~15,000 filas x ~1,900 columnas
  Despues de filtrar: ~600 filas x 11 columnas
...
--- Paso 2/2: Analisis ---
Generando graficos...
  Guardado: output/figuras/evolucion_democracia.png
  Guardado: output/figuras/evolucion_pib_percapita.png
  Guardado: output/figuras/correlaciones.png
  Guardado: output/figuras/barras_democracia.png
  Guardado: output/figuras/scatter_pib_percapita_vs_democracia.png

PIPELINE COMPLETADO en X.X segundos
```

Comprueba que en `output/figuras/` tienes 5 imagenes PNG con graficos correctos.

---

## Paso 7: Escribir tu informe

Crea un archivo `INFORME.md` con:

1. **Introduccion:** Que pregunta intentas responder y por que
2. **Datos:** De donde vienen, que variables elegiste, que periodo
3. **Metodologia:** Que pasos de limpieza aplicaste y por que
4. **Resultados:** Incluye tus graficos con interpretacion
5. **Conclusiones:** Que encontraste, limitaciones del analisis

Ejemplo de como incluir una imagen en Markdown:

```markdown
## Evolucion de la Democracia

![Democracia en America Latina](output/figuras/evolucion_democracia.png)

Se observa que Chile y Uruguay mantienen los niveles mas altos de democracia
en la region, mientras que Venezuela muestra un descenso marcado a partir de 2005...
```

---

## Estructura final de tu entrega

```
entregas/trabajo_final/TU_USUARIO/
├── main.py              # Script principal (orquestador)
├── etl.py               # Modulo de limpieza y preparacion
├── analisis.py          # Modulo de analisis y visualizacion
├── INFORME.md           # Tu reporte con hallazgos
├── requirements.txt     # Librerias necesarias
└── output/
    ├── datos_limpios.parquet
    └── figuras/
        ├── evolucion_democracia.png
        ├── evolucion_pib_percapita.png
        ├── correlaciones.png
        ├── barras_democracia.png
        └── scatter_pib_percapita_vs_democracia.png
```

---

## Extras: Para ir mas alla

### Clustering (Machine Learning)

Si quieres agrupar paises por similitud, anade esto a tu `analisis.py`:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def clustering_paises(df, variables, n_clusters=4):
    """Agrupa paises con K-Means sobre el ultimo anio disponible."""
    # Preparar datos: un snapshot por pais
    ultimo = df.dropna(subset=variables)
    ultimo = ultimo.sort_values("anio").groupby("pais").last().reset_index()

    # Escalar variables (media=0, std=1)
    scaler = StandardScaler()
    X = scaler.fit_transform(ultimo[variables])

    # K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    ultimo["cluster"] = kmeans.fit_predict(X)

    print(f"\nClusters encontrados ({n_clusters}):")
    for c in range(n_clusters):
        paises = ultimo[ultimo["cluster"] == c]["pais"].tolist()
        print(f"  Cluster {c}: {', '.join(paises)}")

    return ultimo
```

### Cargar a PostgreSQL

Si tienes Docker con PostgreSQL corriendo (ver `README_INFRAESTRUCTURA.md`):

```python
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:password@localhost:5432/bigdata_db")
df.to_sql("qog_datos", engine, if_exists="replace", index=False)
print("Datos cargados en PostgreSQL")
```

### Usar Dask para escalabilidad

Reemplaza `pandas.read_csv` por `dask.dataframe.read_csv` para simular
procesamiento Big Data:

```python
import dask.dataframe as dd

ddf = dd.read_csv("datos/qog/qog_std_ts_jan24.csv")
# Las operaciones son lazy (no se ejecutan hasta .compute())
resultado = ddf[ddf["cname"] == "Spain"]["vdem_polyarchy"].mean().compute()
```

---

## Preguntas frecuentes

**El CSV tarda mucho en cargar.**
Es normal la primera vez (~10 segundos). Una vez guardado como Parquet, las
lecturas posteriores son mucho mas rapidas (~0.5 segundos).

**No encuentro la variable que busco.**
El QoG tiene ~1,900 columnas. Consulta el codebook oficial:
https://www.qog.pol.gu.se/data/datadownloads/qogstandarddata
Busca en la seccion "Codebook" el PDF con todas las variables.

**Tengo muchos valores nulos.**
Es normal. No todos los paises tienen datos para todos los anios y variables.
Algunas variables (como V-Dem) tienen datos desde 1900, otras (como CPI) solo
desde 1995. Filtra por periodos donde tus variables tengan buena cobertura.

**Mi grafico no muestra todos los paises.**
Verifica que los nombres de paises coinciden exactamente con los del QoG.
Usa `df["cname"].unique()` para ver los nombres disponibles.

---

## Referencias

- Teorell, J. et al. (2024). *The Quality of Government Standard Dataset* (version Jan24). University of Gothenburg. https://www.qog.pol.gu.se
- McKinney, W. (2017). *Python for Data Analysis*. O'Reilly Media.
- VanderPlas, J. (2016). *Python Data Science Handbook*. O'Reilly Media.

---

*Guia creada para el curso de Big Data con Python - Prof. Juan Marcelo Gutierrez Miranda*
