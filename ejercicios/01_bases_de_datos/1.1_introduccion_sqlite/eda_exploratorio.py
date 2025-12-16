
import pandas as pd
import glob
import os
from pathlib import Path

def analizar_calidad_y_contenido(dataframe):
    """
    Analiza calidad (nulos, duplicados) y contenido (rangos, valores únicos).
    """
    calidad = {
        'filas_duplicadas': int(dataframe.duplicated().sum()),
        'columnas': []
    }

    for col in dataframe.columns:
        col_info = {
            'nombre': col,
            'tipo': str(dataframe[col].dtype),
            'nulos': int(dataframe[col].isna().sum()),
            'nulos_pct': (dataframe[col].isna().sum() / len(dataframe)) * 100 if len(dataframe) > 0 else 0,
            'valores_unicos': dataframe[col].nunique()
        }

        # Análisis específico para tipos de datos
        if pd.api.types.is_numeric_dtype(dataframe[col].dtype):
            col_info['rango'] = {
                'min': dataframe[col].min(),
                'max': dataframe[col].max(),
                'promedio': dataframe[col].mean()
            }
        
        calidad['columnas'].append(col_info)
        
    return calidad

def extraer_fabricantes(dataframe, columna_nombre='name'):
    """Extrae fabricantes únicos del nombre del producto (primera palabra)."""
    if columna_nombre not in dataframe.columns:
        return set()
    
    # Ignorar errores en caso de que la columna no sea de texto
    try:
        fabricantes = dataframe[columna_nombre].str.split().str[0].dropna().unique()
        return set(fabricantes)
    except AttributeError:
        return set()

def extraer_colores(dataframe):
    """Extrae colores únicos si existe una columna 'color'."""
    colores = set()
    columna_color = next((col for col in dataframe.columns if 'color' in col.lower()), None)
    
    if columna_color:
        colores.update(dataframe[columna_color].dropna().unique())
        
    return colores

def generar_reporte_completo(ruta_carpeta_csv, ruta_salida_txt):
    """
    Genera un reporte completo de todos los CSVs, lo imprime y lo guarda en un archivo.
    """
    archivos_csv = sorted(glob.glob(os.path.join(ruta_carpeta_csv, "*.csv")))
    
    if not archivos_csv:
        print(f"Error: No se encontraron archivos CSV en la ruta: {ruta_carpeta_csv}")
        return

    reporte_final = []
    todos_fabricantes = set()
    todos_colores = set()
    lista_de_columnas = []
    categorias_detectadas = []

    reporte_final.append("=" * 80)
    reporte_final.append("INICIO DEL ANÁLISIS EXPLORATORIO DE DATOS (EDA)")
    reporte_final.append("=" * 80)

    # 1. Análisis por archivo
    for ruta_csv in archivos_csv:
        nombre_archivo = Path(ruta_csv).stem
        categorias_detectadas.append(nombre_archivo)
        
        try:
            df = pd.read_csv(ruta_csv)
            lista_de_columnas.append(set(df.columns))

            reporte_final.append(f"\n--- Archivo: {nombre_archivo}.csv ---")
            reporte_final.append(f"1. Análisis Básico:")
            reporte_final.append(f"   - Dimensiones: {df.shape[0]} filas, {df.shape[1]} columnas")
            reporte_final.append(f"   - Filas duplicadas: {df.duplicated().sum()}")
            reporte_final.append(f"   - Ejemplo de datos (primeras 3 filas):\n{df.head(3).to_string()}\n")

            # Calidad y contenido
            analisis = analizar_calidad_y_contenido(df)
            reporte_final.append(f"2. Análisis de Columnas y Calidad:")
            for col_info in analisis['columnas']:
                reporte_final.append(f"   - Columna: '{col_info['nombre']}'")
                reporte_final.append(f"     - Tipo: {col_info['tipo']}")
                reporte_final.append(f"     - Nulos: {col_info['nulos']} ({col_info['nulos_pct']:.2f}%)")
                reporte_final.append(f"     - Valores únicos: {col_info['valores_unicos']}")
                if 'rango' in col_info:
                    r = col_info['rango']
                    reporte_final.append(f"     - Rango numérico: Min={r['min']:.2f}, Max={r['max']:.2f}, Promedio={r['promedio']:.2f}")

            # Patrones
            todos_fabricantes.update(extraer_fabricantes(df))
            todos_colores.update(extraer_colores(df))

        except Exception as e:
            reporte_final.append(f"\n--- Archivo: {nombre_archivo}.csv ---")
            reporte_final.append(f"   [ERROR] No se pudo procesar el archivo: {e}")

    # 3. Análisis de patrones (resumen)
    columnas_comunes = set.intersection(*lista_de_columnas) if lista_de_columnas else set()

    reporte_final.append("\n" + "=" * 80)
    reporte_final.append("RESUMEN GENERAL DEL ANÁLISIS")
    reporte_final.append("=" * 80)
    reporte_final.append(f"\nTotal de archivos analizados: {len(archivos_csv)}")
    
    reporte_final.append("\n3. Análisis de Patrones:")
    reporte_final.append(f"   - Categorías detectadas (por nombre de archivo): {len(categorias_detectadas)}")
    reporte_final.append(f"   - Fabricantes únicos extraídos: {len(todos_fabricantes)}")
    reporte_final.append(f"   - Colores únicos encontrados: {len(todos_colores)}")
    reporte_final.append(f"   - Columnas comunes en TODOS los archivos: {', '.join(columnas_comunes) if columnas_comunes else 'Ninguna'}")

    # 4. Salida
    reporte_completo_str = "\n".join(reporte_final)
    print(reporte_completo_str)

    try:
        with open(ruta_salida_txt, 'w', encoding='utf-8') as f:
            f.write(reporte_completo_str)
        print(f"\n[OK] Reporte guardado exitosamente en: {ruta_salida_txt}")
    except Exception as e:
        print(f"\n[ERROR] No se pudo guardar el reporte en archivo: {e}")


if __name__ == "__main__":
    # Define las rutas de manera robusta
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_datos = os.path.join(BASE_DIR, "../../../datos/csv_tienda_informatica")
    ruta_salida = os.path.join(BASE_DIR, "resumen_eda.txt")
    
    generar_reporte_completo(ruta_datos, ruta_salida)
