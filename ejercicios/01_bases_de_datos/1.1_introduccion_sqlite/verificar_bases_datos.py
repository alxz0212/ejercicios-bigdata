import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def verificar_modelo_a():
    print("\n--- Verificando Modelo A (tienda_modelo_a.db) ---")
    db_path = os.path.join(BASE_DIR, 'tienda_modelo_a.db')
    if not os.path.exists(db_path):
        print("ERROR: No existe el archivo de base de datos.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Contar tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()
    print(f"Total de tablas encontradas: {len(tablas)}")
    
    # Verificar algunas tablas específicas
    tablas_check = ['cpu', 'motherboard', 'video_card']
    for tabla in tablas_check:
        tabla_nombre = tabla  # En modelo A los nombres son tal cual el CSV (con guiones bajos si se reemplazaron)
        # Buscar nombre real en la lista
        nombre_real = next((t[0] for t in tablas if t[0] == tabla), None)
        
        if nombre_real:
            cursor.execute(f"SELECT COUNT(*) FROM {nombre_real}")
            count = cursor.fetchone()[0]
            print(f"  Tabla '{nombre_real}': {count} filas")
        else:
            print(f"  [!] Tabla '{tabla}' no encontrada (¿quizás tiene otro nombre?)")

    conn.close()

def verificar_modelo_b():
    print("\n--- Verificando Modelo B (tienda_modelo_b.db) ---")
    db_path = os.path.join(BASE_DIR, 'tienda_modelo_b.db')
    if not os.path.exists(db_path):
        print("ERROR: No existe el archivo de base de datos.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Contar registros principales
    cursor.execute("SELECT COUNT(*) FROM productos")
    n_prod = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM categorias")
    n_cat = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM fabricantes")
    n_fab = cursor.fetchone()[0]
    
    print(f"Resumen de datos:")
    print(f"  Productos: {n_prod}")
    print(f"  Categorías: {n_cat}")
    print(f"  Fabricantes: {n_fab}")
    
    # Prueba de JOIN (Relaciones)
    print("\nPrueba de consulta con JOIN (Primeros 3 productos):")
    query = """
        SELECT p.nombre, c.nombre as categoria, f.nombre as fabricante, p.precio
        FROM productos p
        JOIN categorias c ON p.categoria_id = c.id
        JOIN fabricantes f ON p.fabricante_id = f.id
        LIMIT 3
    """
    try:
        cursor.execute(query)
        filas = cursor.fetchall()
        for fila in filas:
            print(f"  - {fila[0]} | Cat: {fila[1]} | Fab: {fila[2]} | ${fila[3]}")
    except Exception as e:
        print(f"  [ERROR] Falló la consulta JOIN: {e}")

    conn.close()

def verificar_modelo_c():
    print("\n--- Verificando Modelo C (tienda_modelo_c.db) ---")
    db_path = os.path.join(BASE_DIR, 'tienda_modelo_c.db')
    if not os.path.exists(db_path):
        print("ERROR: No existe el archivo de base de datos.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Verificar tablas nuevas
    tablas_nuevas = ['clientes', 'pedidos', 'lineas_pedido', 'inventario']
    print("Verificando tablas del sistema E-commerce:")
    for tabla in tablas_nuevas:
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tabla}';")
        existe = cursor.fetchone()
        status = "OK" if existe else "FALTA"
        print(f"  Tabla '{tabla}': {status}")
        
    # Verificar datos en inventario
    cursor.execute("SELECT COUNT(*) FROM inventario")
    n_inv = cursor.fetchone()[0]
    print(f"Registros en inventario: {n_inv} (Debería ser igual al número de productos)")
    
    conn.close()

if __name__ == "__main__":
    verificar_modelo_a()
    verificar_modelo_b()
    verificar_modelo_c()
