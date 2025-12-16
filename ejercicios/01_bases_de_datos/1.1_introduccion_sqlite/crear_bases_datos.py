import sqlite3
import pandas as pd
import os
import glob
from pathlib import Path

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DATOS = os.path.join(BASE_DIR, "../../../datos/csv_tienda_informatica")

def get_db_connection(db_name):
    """Crea una conexión a la base de datos SQLite"""
    db_path = os.path.join(BASE_DIR, db_name)
    conn = sqlite3.connect(db_path)
    return conn

def crear_modelo_a():
    """
    Modelo A: Catálogo Simple (Desnormalizado)
    Carga cada CSV como una tabla independiente.
    """
    print(f"\nGenerando Modelo A (tienda_modelo_a.db)...")
    conn = get_db_connection('tienda_modelo_a.db')
    
    archivos_csv = glob.glob(os.path.join(RUTA_DATOS, "*.csv"))
    
    for ruta_csv in archivos_csv:
        nombre_archivo = Path(ruta_csv).stem
        # Limpiar nombre de tabla (reemplazar guiones por guiones bajos)
        nombre_tabla = nombre_archivo.replace('-', '_')
        
        df = pd.read_csv(ruta_csv)
        
        # Guardar en SQLite
        df.to_sql(nombre_tabla, conn, if_exists='replace', index=False)
        print(f"  - Tabla creada: {nombre_tabla} ({len(df)} filas)")
        
    conn.close()
    print("Modelo A completado.")

def crear_modelo_b():
    """
    Modelo B: Normalizado (3NF)
    Esquema: categorias, fabricantes, productos, colores, productos_colores
    """
    print(f"\nGenerando Modelo B (tienda_modelo_b.db)...")
    conn = get_db_connection('tienda_modelo_b.db')
    cursor = conn.cursor()
    
    # 1. Crear Esquema
    cursor.executescript("""
        DROP TABLE IF EXISTS productos_colores;
        DROP TABLE IF EXISTS colores;
        DROP TABLE IF EXISTS productos;
        DROP TABLE IF EXISTS fabricantes;
        DROP TABLE IF EXISTS categorias;
        
        CREATE TABLE categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL
        );
        
        CREATE TABLE fabricantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL
        );
        
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL,
            categoria_id INTEGER,
            fabricante_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias (id),
            FOREIGN KEY (fabricante_id) REFERENCES fabricantes (id)
        );
        
        CREATE TABLE colores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL
        );
        
        CREATE TABLE productos_colores (
            producto_id INTEGER,
            color_id INTEGER,
            PRIMARY KEY (producto_id, color_id),
            FOREIGN KEY (producto_id) REFERENCES productos (id),
            FOREIGN KEY (color_id) REFERENCES colores (id)
        );
    """)
    
    # 2. Popular Datos
    archivos_csv = glob.glob(os.path.join(RUTA_DATOS, "*.csv"))
    
    # Diccionarios para cachear IDs y evitar consultas repetitivas
    mapa_categorias = {} # nombre -> id
    mapa_fabricantes = {} # nombre -> id
    
    for ruta_csv in archivos_csv:
        nombre_archivo = Path(ruta_csv).stem
        nombre_categoria = nombre_archivo.replace('-', ' ').title()
        
        # Insertar Categoría
        if nombre_categoria not in mapa_categorias:
            cursor.execute("INSERT OR IGNORE INTO categorias (nombre) VALUES (?)", (nombre_categoria,))
            # Recuperar ID (ya sea el insertado o el existente)
            cursor.execute("SELECT id FROM categorias WHERE nombre = ?", (nombre_categoria,))
            mapa_categorias[nombre_categoria] = cursor.fetchone()[0]
            
        cat_id = mapa_categorias[nombre_categoria]
        
        # Leer CSV
        df = pd.read_csv(ruta_csv)
        
        # Procesar cada producto
        productos_data = []
        
        for _, row in df.iterrows():
            nombre_producto = row.get('name', 'Desconocido')
            precio = row.get('price', 0.0)
            
            # Extraer Fabricante (Primera palabra del nombre)
            nombre_fabricante = str(nombre_producto).split()[0] if nombre_producto else "Genérico"
            
            # Insertar Fabricante si no existe
            if nombre_fabricante not in mapa_fabricantes:
                cursor.execute("INSERT OR IGNORE INTO fabricantes (nombre) VALUES (?)", (nombre_fabricante,))
                cursor.execute("SELECT id FROM fabricantes WHERE nombre = ?", (nombre_fabricante,))
                res = cursor.fetchone()
                if res:
                    mapa_fabricantes[nombre_fabricante] = res[0]
                else:
                    continue # Skip si falla
            
            fab_id = mapa_fabricantes[nombre_fabricante]
            
            # Preparar tupla para inserción masiva de productos
            productos_data.append((nombre_producto, precio, cat_id, fab_id))
            
            # NOTA: La lógica de colores se omite aquí porque la mayoría de CSVs 
            # de hardware no tienen columna 'color' explícita estándar. 
            # Si existiera, se procesaría aquí insertando en 'colores' y 'productos_colores'.

        # Insertar productos en lote
        cursor.executemany("""
            INSERT INTO productos (nombre, precio, categoria_id, fabricante_id) 
            VALUES (?, ?, ?, ?)
        """, productos_data)
        
    conn.commit()
    
    # Verificar conteos
    cursor.execute("SELECT COUNT(*) FROM productos")
    total_prod = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM fabricantes")
    total_fab = cursor.fetchone()[0]
    
    print(f"  - Datos insertados: {total_prod} productos, {total_fab} fabricantes.")
    conn.close()
    print("Modelo B completado.")

def crear_modelo_c():
    """
    Modelo C: E-Commerce Completo
    Hereda datos del Modelo B y añade tablas de negocio (Clientes, Pedidos, etc.)
    """
    print(f"\nGenerando Modelo C (tienda_modelo_c.db)...")
    
    # Primero, copiamos la estructura y datos del B al C para no repetir el proceso ETL
    # O simplemente ejecutamos la lógica de B sobre la base de datos C
    
    conn = get_db_connection('tienda_modelo_c.db')
    cursor = conn.cursor()
    
    # --- PARTE 1: REPLICAR MODELO B (Esquema y Datos) ---
    # (Simplificado: llamamos a la lógica de creación de tablas de nuevo)
    # En un entorno real, podríamos copiar el archivo .db, pero aquí lo haremos por SQL
    
    # Esquema Base (Igual que B)
    cursor.executescript("""
        DROP TABLE IF EXISTS items_carrito;
        DROP TABLE IF EXISTS carritos;
        DROP TABLE IF EXISTS lineas_pedido;
        DROP TABLE IF EXISTS pedidos;
        DROP TABLE IF EXISTS clientes;
        DROP TABLE IF EXISTS inventario;
        DROP TABLE IF EXISTS productos_colores;
        DROP TABLE IF EXISTS colores;
        DROP TABLE IF EXISTS productos;
        DROP TABLE IF EXISTS fabricantes;
        DROP TABLE IF EXISTS categorias;
        
        -- Tablas del Modelo B
        CREATE TABLE categorias (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT UNIQUE);
        CREATE TABLE fabricantes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT UNIQUE);
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT, 
            precio REAL, 
            categoria_id INTEGER, 
            fabricante_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id),
            FOREIGN KEY (fabricante_id) REFERENCES fabricantes(id)
        );
        CREATE TABLE colores (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT UNIQUE);
        CREATE TABLE productos_colores (
            producto_id INTEGER, color_id INTEGER,
            PRIMARY KEY (producto_id, color_id),
            FOREIGN KEY (producto_id) REFERENCES productos(id),
            FOREIGN KEY (color_id) REFERENCES colores(id)
        );
    """)
    
    # --- PARTE 2: AÑADIR NUEVAS TABLAS (Modelo C) ---
    cursor.executescript("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            nombre TEXT NOT NULL,
            direccion TEXT,
            fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            fecha_pedido DATETIME DEFAULT CURRENT_TIMESTAMP,
            estado TEXT DEFAULT 'pendiente', -- pendiente, enviado, entregado
            total REAL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );

        CREATE TABLE lineas_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario REAL NOT NULL,
            FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
            FOREIGN KEY (producto_id) REFERENCES productos(id)
        );

        CREATE TABLE carritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER UNIQUE, -- Un carrito por cliente (o null para invitados)
            fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );

        CREATE TABLE items_carrito (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            carrito_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER DEFAULT 1,
            FOREIGN KEY (carrito_id) REFERENCES carritos(id),
            FOREIGN KEY (producto_id) REFERENCES productos(id)
        );
        
        CREATE TABLE inventario (
            producto_id INTEGER PRIMARY KEY,
            stock_disponible INTEGER DEFAULT 0,
            ultima_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (producto_id) REFERENCES productos(id)
        );
    """)
    
    # --- PARTE 3: MIGRAR DATOS (Reutilizando lógica similar a B) ---
    # Para no duplicar código complejo, aquí haremos una carga simplificada 
    # leyendo los CSVs de nuevo para poblar productos/categorias/fabricantes
    
    archivos_csv = glob.glob(os.path.join(RUTA_DATOS, "*.csv"))
    mapa_categorias = {}
    mapa_fabricantes = {}
    
    for ruta_csv in archivos_csv:
        nombre_categoria = Path(ruta_csv).stem.replace('-', ' ').title()
        
        if nombre_categoria not in mapa_categorias:
            cursor.execute("INSERT OR IGNORE INTO categorias (nombre) VALUES (?)", (nombre_categoria,))
            cursor.execute("SELECT id FROM categorias WHERE nombre = ?", (nombre_categoria,))
            mapa_categorias[nombre_categoria] = cursor.fetchone()[0]
        
        cat_id = mapa_categorias[nombre_categoria]
        df = pd.read_csv(ruta_csv)
        
        productos_data = []
        for _, row in df.iterrows():
            nombre_prod = row.get('name', 'Desc')
            precio = row.get('price', 0)
            fab = str(nombre_prod).split()[0] if nombre_prod else "Gen"
            
            if fab not in mapa_fabricantes:
                cursor.execute("INSERT OR IGNORE INTO fabricantes (nombre) VALUES (?)", (fab,))
                cursor.execute("SELECT id FROM fabricantes WHERE nombre = ?", (fab,))
                res = cursor.fetchone()
                if res: mapa_fabricantes[fab] = res[0]
            
            if fab in mapa_fabricantes:
                productos_data.append((nombre_prod, precio, cat_id, mapa_fabricantes[fab]))
        
        cursor.executemany("INSERT INTO productos (nombre, precio, categoria_id, fabricante_id) VALUES (?, ?, ?, ?)", productos_data)
        
    # Inicializar inventario (Dummy data: 10 unidades para cada producto)
    cursor.execute("INSERT INTO inventario (producto_id, stock_disponible) SELECT id, 10 FROM productos")
    
    conn.commit()
    conn.close()
    print("Modelo C completado.")

if __name__ == "__main__":
    if not os.path.exists(RUTA_DATOS):
        print(f"ERROR: No se encuentra la ruta de datos: {RUTA_DATOS}")
    else:
        # crear_modelo_a()
        # crear_modelo_b()
        crear_modelo_c()
        print("\n¡Proceso finalizado! Se ha creado la base de datos del Modelo C.")
