"""
Script para crear y poblar la base de datos 'jardineria.db'
Usa SQLite y la librería Faker para generar datos ficticios.
"""

import sqlite3
from faker import Faker
import random
from pathlib import Path
import os

# --- CONFIGURACIÓN ---
fake = Faker('es_ES')  # Datos en español
CANTIDAD_DATOS = 20

# --- RUTA ABSOLUTA Y SEGURA ---
DIRECTORIO_SCRIPT = Path(__file__).parent.resolve()
RUTA_DB = DIRECTORIO_SCRIPT / "jardineria.db"


def crear_tablas(cursor):
    # Habilitar Foreign Keys
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Tabla oficina
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS oficina (
        codigo_oficina TEXT PRIMARY KEY,
        ciudad TEXT NOT NULL,
        pais TEXT NOT NULL,
        region TEXT,
        codigo_postal TEXT NOT NULL,
        telefono TEXT NOT NULL,
        linea_direccion1 TEXT NOT NULL,
        linea_direccion2 TEXT
    );
    """)

    # 2. Tabla empleado
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleado (
        codigo_empleado INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido1 TEXT NOT NULL,
        apellido2 TEXT,
        extension TEXT NOT NULL,
        email TEXT NOT NULL,
        codigo_oficina TEXT NOT NULL,
        codigo_jefe INTEGER,
        puesto TEXT,
        FOREIGN KEY (codigo_oficina) REFERENCES oficina(codigo_oficina),
        FOREIGN KEY (codigo_jefe) REFERENCES empleado(codigo_empleado)
    );
    """)

    # 3. Tabla gama_producto
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gama_producto (
        gama TEXT PRIMARY KEY,
        descripcion_texto TEXT,
        descripcion_html TEXT,
        imagen TEXT
    );
    """)

    # 4. Tabla cliente
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        codigo_cliente INTEGER PRIMARY KEY,
        nombre_cliente TEXT NOT NULL,
        nombre_contacto TEXT,
        apellido_contacto TEXT,
        telefono TEXT NOT NULL,
        fax TEXT NOT NULL,
        linea_direccion1 TEXT NOT NULL,
        linea_direccion2 TEXT,
        ciudad TEXT NOT NULL,
        region TEXT,
        pais TEXT,
        codigo_postal TEXT,
        codigo_empleado_rep_ventas INTEGER,
        limite_credito REAL,
        FOREIGN KEY (codigo_empleado_rep_ventas) REFERENCES empleado(codigo_empleado)
    );
    """)

    # 5. Tabla pedido
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedido (
        codigo_pedido INTEGER PRIMARY KEY,
        fecha_pedido DATE NOT NULL,
        fecha_esperada DATE NOT NULL,
        fecha_entrega DATE,
        estado TEXT NOT NULL,
        comentarios TEXT,
        codigo_cliente INTEGER NOT NULL,
        FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo_cliente)
    );
    """)

    # 6. Tabla producto
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS producto (
        codigo_producto TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        gama TEXT NOT NULL,
        dimensiones TEXT,
        proveedor TEXT,
        descripcion TEXT,
        cantidad_en_stock INTEGER NOT NULL,
        precio_venta REAL NOT NULL,
        precio_proveedor REAL,
        FOREIGN KEY (gama) REFERENCES gama_producto(gama)
    );
    """)

    # 7. Tabla detalle_pedido
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detalle_pedido (
        codigo_pedido INTEGER,
        codigo_producto TEXT,
        cantidad INTEGER NOT NULL,
        precio_unidad REAL NOT NULL,
        numero_linea INTEGER NOT NULL,
        PRIMARY KEY (codigo_pedido, codigo_producto),
        FOREIGN KEY (codigo_pedido) REFERENCES pedido(codigo_pedido),
        FOREIGN KEY (codigo_producto) REFERENCES producto(codigo_producto)
    );
    """)

    # 8. Tabla pago
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pago (
        id_transaccion TEXT PRIMARY KEY,
        codigo_cliente INTEGER NOT NULL,
        forma_pago TEXT NOT NULL,
        fecha_pago DATE NOT NULL,
        total REAL NOT NULL,
        FOREIGN KEY (codigo_cliente) REFERENCES cliente(codigo_cliente)
    );
    """)
    print("✅ Tablas creadas correctamente.")

def poblar_datos(cursor):
    print("🔄 Generando datos ficticios...")

    # --- 1. Oficinas ---
    oficinas_ids = []
    for i in range(CANTIDAD_DATOS):
        cod = f"OF-{i+1:03d}"
        oficinas_ids.append(cod)
        cursor.execute("INSERT OR IGNORE INTO oficina VALUES (?,?,?,?,?,?,?,?)", (
            cod, fake.city(), fake.country(), fake.state(), fake.postcode(),
            fake.phone_number(), fake.street_address(), fake.secondary_address()
        ))

    # --- 2. Empleados ---
    empleados_ids = []
    # Primero creamos un "Jefe Supremo" (sin jefe)
    # CORREGIDO: 9 valores para 9 columnas
    cursor.execute("INSERT OR IGNORE INTO empleado VALUES (?,?,?,?,?,?,?,?,?)", (
        1, fake.first_name(), fake.last_name(), fake.last_name(), "0000",
        fake.email(), random.choice(oficinas_ids), None, "Director General"
    ))
    empleados_ids.append(1)

    # El resto de empleados
    for i in range(2, CANTIDAD_DATOS + 1):
        jefe = random.choice(empleados_ids) # Reporta a alguien ya creado
        # CORREGIDO: 9 valores para 9 columnas
        cursor.execute("INSERT OR IGNORE INTO empleado VALUES (?,?,?,?,?,?,?,?,?)", (
            i, fake.first_name(), fake.last_name(), fake.last_name(),
            str(random.randint(1000, 9999)), fake.email(),
            random.choice(oficinas_ids), jefe, fake.job()
        ))
        empleados_ids.append(i)

    # --- 3. Gamas ---
    gamas = ['Herramientas', 'Frutales', 'Ornamentales', 'Riego', 'Mobiliario']
    while len(gamas) < CANTIDAD_DATOS:
        gamas.append(fake.word().capitalize())
    
    for g in gamas[:CANTIDAD_DATOS]:
        cursor.execute("INSERT OR IGNORE INTO gama_producto VALUES (?,?,?,?)", (
            g, fake.text(max_nb_chars=50), "<html>...</html>", f"img/{g}.jpg"
        ))

    # --- 4. Clientes ---
    clientes_ids = []
    for i in range(1, CANTIDAD_DATOS + 1):
        cursor.execute("INSERT OR IGNORE INTO cliente VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            i, fake.company(), fake.first_name(), fake.last_name(),
            fake.phone_number(), fake.phone_number(), fake.street_address(), "",
            fake.city(), fake.state(), fake.country(), fake.postcode(),
            random.choice(empleados_ids), random.uniform(1000, 50000)
        ))
        clientes_ids.append(i)

    # --- 5. Pedidos ---
    pedidos_ids = []
    estados = ['Entregado', 'Pendiente', 'Rechazado', 'En tránsito']
    for i in range(1, CANTIDAD_DATOS + 1):
        f_pedido = fake.date_between(start_date='-1y', end_date='today')
        cursor.execute("INSERT OR IGNORE INTO pedido VALUES (?,?,?,?,?,?,?)", (
            i, f_pedido, fake.date_between(start_date=f_pedido, end_date='+30d'),
            fake.date_between(start_date=f_pedido, end_date='+30d'),
            random.choice(estados), fake.sentence(), random.choice(clientes_ids)
        ))
        pedidos_ids.append(i)

    # --- 6. Productos ---
    productos_ids = []
    for i in range(1, CANTIDAD_DATOS + 1):
        cod = f"PROD-{i:04d}"
        productos_ids.append(cod)
        cursor.execute("INSERT OR IGNORE INTO producto VALUES (?,?,?,?,?,?,?,?,?)", (
            cod, fake.word().capitalize(), random.choice(gamas), "10x20x30",
            fake.company(), fake.sentence(), random.randint(0, 500),
            random.uniform(10, 500), random.uniform(5, 300)
        ))

    # --- 7. Detalle Pedido ---
    for ped_id in pedidos_ids:
        num_items = random.randint(1, 5)
        prods_seleccionados = random.sample(productos_ids, num_items)
        for idx, prod_id in enumerate(prods_seleccionados):
            cursor.execute("INSERT OR IGNORE INTO detalle_pedido VALUES (?,?,?,?,?)", (
                ped_id, prod_id, random.randint(1, 20),
                random.uniform(10, 100), idx + 1
            ))

    # --- 8. Pagos ---
    formas = ['PayPal', 'Transferencia', 'Cheque', 'Tarjeta']
    for i in range(CANTIDAD_DATOS):
        cursor.execute("INSERT OR IGNORE INTO pago VALUES (?,?,?,?,?)", (
            fake.uuid4(), random.choice(clientes_ids), random.choice(formas),
            fake.date_between(start_date='-1y', end_date='today'),
            random.uniform(50, 5000)
        ))

    print(f"✅ Se han insertado {CANTIDAD_DATOS} registros (aprox) en cada tabla.")

def main():
    print(f"Intentando crear la base de datos en: {RUTA_DB}")
    
    # Opcional: Borrar la base de datos anterior para empezar de cero
    if RUTA_DB.exists():
        try:
            RUTA_DB.unlink()
            print("🗑️ Base de datos anterior eliminada.")
        except OSError as e:
            print(f"❌ Error al eliminar la base de datos anterior: {e}")
            return

    conn = None
    try:
        conn = sqlite3.connect(RUTA_DB)
        cursor = conn.cursor()
        
        crear_tablas(cursor)
        poblar_datos(cursor)
        
        conn.commit()
        print(f"\n🚀 Base de datos creada exitosamente en:\n   {RUTA_DB}")
        
    except Exception as e:
        print(f"❌ Ocurrió un error grave: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
