"""
Script de Análisis Exploratorio de Datos (EDA) para la base de datos 'jardineria.db'.
Genera un reporte detallado sobre la estructura, calidad y patrones de los datos.
"""

import sqlite3
import pandas as pd
from pathlib import Path
import io

# --- CONFIGURACIÓN ---
DIRECTORIO_SCRIPT = Path(__file__).parent.resolve()
RUTA_DB = DIRECTORIO_SCRIPT / "jardineria.db"
RUTA_REPORTE = DIRECTORIO_SCRIPT / "resumen_jardineria_eda.md"

# Buffer para guardar el reporte
reporte_buffer = []

def log(texto, nivel=0):
    """Agrega texto al buffer del reporte y lo imprime en consola."""
    prefix = "#" * nivel + " " if nivel > 0 else ""
    linea = f"{prefix}{texto}"
    print(linea)
    reporte_buffer.append(linea)

def log_bloque(texto):
    """Agrega un bloque de código/texto al reporte."""
    print(texto)
    reporte_buffer.append(f"```text\n{texto}\n```")

def analizar_tabla(nombre_tabla, conn):
    log(f"Tabla: {nombre_tabla}", 2)
    
    try:
        df = pd.read_sql_query(f"SELECT * FROM {nombre_tabla}", conn)
        
        # 1. Análisis General
        filas, cols = df.shape
        log(f"- **Dimensiones:** {filas} filas x {cols} columnas")
        
        # Tipos de datos
        buffer_info = io.StringIO()
        df.info(buf=buffer_info)
        log("- **Estructura y Tipos de Datos:**")
        log_bloque(buffer_info.getvalue().split('\n')[0:-3]) # Limpiamos un poco la salida
        
        # Primeras filas
        log("- **Ejemplo de Datos (Primeras 3 filas):**")
        log_bloque(df.head(3).to_string(index=False))
        
        # 2. Calidad de Datos
        log("- **Análisis de Calidad:**")
        
        # Nulos
        nulos = df.isnull().sum()
        nulos_pct = (df.isnull().sum() / len(df)) * 100
        df_nulos = pd.DataFrame({'Nulos': nulos, '% Nulos': nulos_pct})
        if df_nulos['Nulos'].sum() > 0:
            log("  - **Valores Nulos detectados:**")
            log_bloque(df_nulos[df_nulos['Nulos'] > 0].to_string())
        else:
            log("  - ✅ No se detectaron valores nulos.")
            
        # Duplicados
        duplicados = df.duplicated().sum()
        if duplicados > 0:
            log(f"  - ⚠️ **Filas duplicadas:** {duplicados}")
        else:
            log("  - ✅ No hay filas completamente duplicadas.")
            
        # 3. Estadísticas Numéricas
        cols_num = df.select_dtypes(include=['number']).columns
        if not cols_num.empty:
            log("- **Estadísticas Numéricas (Min, Max, Promedio):**")
            log_bloque(df[cols_num].describe().loc[['min', 'max', 'mean']].to_string())
            
        # 4. Valores Únicos (Categóricos)
        cols_cat = df.select_dtypes(include=['object']).columns
        if not cols_cat.empty:
            log("- **Valores Únicos en Columnas de Texto (Top 5):**")
            for col in cols_cat:
                unicos = df[col].nunique()
                ejemplos = df[col].unique()[:5]
                log(f"  - `{col}`: {unicos} valores únicos. Ej: {', '.join(map(str, ejemplos))}...")
        
        log("\n---")
        return df.columns.tolist()
        
    except Exception as e:
        log(f"❌ Error analizando tabla {nombre_tabla}: {e}")
        return []

def analisis_patrones_especificos(conn):
    log("Análisis de Patrones Específicos", 2)
    
    # 1. Fabricantes / Proveedores
    try:
        df_prod = pd.read_sql_query("SELECT proveedor, nombre FROM producto", conn)
        proveedores = df_prod['proveedor'].unique()
        log(f"- **Proveedores Identificados ({len(proveedores)}):**")
        log(f"  - {', '.join(proveedores[:10])} ...")
    except:
        pass

    # 2. Colores (Buscando en columnas o descripciones)
    # Como no hay columna 'color' explícita en el esquema creado, buscamos en descripción
    try:
        df_prod = pd.read_sql_query("SELECT descripcion FROM producto", conn)
        # Búsqueda simple de palabras de color en la descripción
        colores_comunes = ['rojo', 'azul', 'verde', 'negro', 'blanco', 'amarillo']
        colores_encontrados = set()
        for desc in df_prod['descripcion'].dropna():
            for color in colores_comunes:
                if color in desc.lower():
                    colores_encontrados.add(color)
        
        if colores_encontrados:
            log(f"- **Colores detectados en descripciones:** {', '.join(colores_encontrados)}")
        else:
            log("- **Colores:** No se detectó columna 'color' ni menciones obvias en descripciones.")
    except:
        pass

def main():
    if not RUTA_DB.exists():
        print(f"❌ Error: No se encuentra la base de datos en {RUTA_DB}")
        return

    conn = sqlite3.connect(RUTA_DB)
    
    log("# Reporte EDA: Base de Datos Jardinería\n")
    log(f"**Archivo analizado:** `{RUTA_DB.name}`\n")
    
    # Obtener lista de tablas
    tablas = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)['name'].tolist()
    log(f"**Tablas encontradas:** {', '.join(tablas)}\n")
    
    todas_columnas = []
    
    # Analizar cada tabla
    for tabla in tablas:
        cols = analizar_tabla(tabla, conn)
        todas_columnas.extend(cols)
        
    # Análisis de columnas comunes
    from collections import Counter
    conteo_cols = Counter(todas_columnas)
    cols_comunes = [col for col, count in conteo_cols.items() if count > 1]
    
    log("Análisis de Relaciones", 2)
    log("- **Columnas Comunes (Posibles Claves Foráneas):**")
    log(f"  - {', '.join(cols_comunes)}")
    
    # Patrones específicos
    analisis_patrones_especificos(conn)
    
    conn.close()
    
    # Guardar reporte
    with open(RUTA_REPORTE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(reporte_buffer))
        
    print(f"\n✅ Reporte guardado exitosamente en: {RUTA_REPORTE}")

if __name__ == "__main__":
    main()
