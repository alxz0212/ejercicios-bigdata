"""
Script para ejecutar consultas SQL sobre la base de datos 'jardineria.db'.
Resuelve los 6 ejercicios propuestos.
"""

import sqlite3
import pandas as pd
from pathlib import Path

# --- CONFIGURACIÓN ---
# Ruta absoluta a la base de datos
DIRECTORIO_SCRIPT = Path(__file__).parent.resolve()
RUTA_DB = DIRECTORIO_SCRIPT / "jardineria.db"

def ejecutar_consulta(sql, titulo, conn):
    print("=" * 80)
    print(f"📌 {titulo}")
    print("-" * 80)
    try:
        # Usamos pandas para leer la consulta SQL y mostrarla bonita
        df = pd.read_sql_query(sql, conn)
        
        if df.empty:
            print("⚠️ No se encontraron resultados para esta consulta.")
        else:
            # Ajustes de visualización de pandas
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', 1000)
            print(df.to_string(index=False))
            
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
    print("\n")

def main():
    if not RUTA_DB.exists():
        print(f"❌ Error: No se encuentra la base de datos en {RUTA_DB}")
        print("   Ejecuta primero 'crear_bd_jardineria.py'")
        return

    # Conectar a la base de datos
    conn = sqlite3.connect(RUTA_DB)

    # --- EJERCICIO 1: Listar todos los clientes de una ciudad específica ---
    sql_1 = """
    SELECT codigo_cliente, nombre_cliente, ciudad, pais 
    FROM cliente 
    ORDER BY ciudad ASC
    LIMIT 15;
    """
    ejecutar_consulta(sql_1, "1. Listar clientes (Muestra de 15 ordenada por ciudad)", conn)


    # --- EJERCICIO 2: Obtener los pedidos que han sido rechazados ---
    sql_2 = """
    SELECT codigo_pedido, fecha_pedido, estado, comentarios 
    FROM pedido 
    WHERE estado = 'Rechazado';
    """
    ejecutar_consulta(sql_2, "2. Pedidos con estado 'Rechazado'", conn)


    # --- EJERCICIO 3: Calcular el total de pagos realizados por cada cliente ---
    sql_3 = """
    SELECT 
        c.nombre_cliente, 
        COUNT(p.id_transaccion) as num_pagos,
        SUM(p.total) as total_pagado
    FROM cliente c
    INNER JOIN pago p ON c.codigo_cliente = p.codigo_cliente
    GROUP BY c.codigo_cliente, c.nombre_cliente
    ORDER BY total_pagado DESC;
    """
    ejecutar_consulta(sql_3, "3. Total de pagos por cliente (Top Pagadores)", conn)


    # --- EJERCICIO 4: Encontrar los productos más caros de cada gama ---
    sql_4 = """
    SELECT 
        p.gama, 
        p.nombre as producto, 
        p.precio_venta
    FROM producto p
    WHERE p.precio_venta = (
        SELECT MAX(p2.precio_venta) 
        FROM producto p2 
        WHERE p2.gama = p.gama
    )
    ORDER BY p.gama;
    """
    ejecutar_consulta(sql_4, "4. Productos más caros de cada gama", conn)


    # --- EJERCICIO 5: Empleados sin clientes asignados (LEFT JOIN) ---
    # Buscamos empleados que no aparecen en la tabla de clientes como representantes de ventas
    sql_5 = """
    SELECT 
        e.nombre, 
        e.apellido1, 
        e.puesto, 
        e.email
    FROM empleado e
    LEFT JOIN cliente c ON e.codigo_empleado = c.codigo_empleado_rep_ventas
    WHERE c.codigo_cliente IS NULL;
    """
    ejecutar_consulta(sql_5, "5. Empleados que NO tienen clientes asignados", conn)


    # --- EJERCICIO 6: Detalle completo de pedidos (JOIN múltiple y cálculos) ---
    # Mostramos qué productos hay en cada pedido y calculamos el subtotal por línea
    sql_6 = """
    SELECT 
        p.codigo_pedido,
        p.fecha_pedido,
        prod.nombre AS producto,
        dp.cantidad,
        dp.precio_unidad,
        (dp.cantidad * dp.precio_unidad) AS subtotal
    FROM pedido p
    INNER JOIN detalle_pedido dp ON p.codigo_pedido = dp.codigo_pedido
    INNER JOIN producto prod ON dp.codigo_producto = prod.codigo_producto
    ORDER BY p.codigo_pedido, dp.numero_linea
    LIMIT 20;
    """
    ejecutar_consulta(sql_6, "6. Detalle de Pedidos con Subtotales (Primeros 20 registros)", conn)

    conn.close()

if __name__ == "__main__":
    main()
