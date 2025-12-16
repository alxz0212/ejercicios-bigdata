"""
Dashboard de E-Commerce (Modelo C) con Flask y Chart.js

Este script crea una aplicación web para visualizar los datos de negocio
del modelo de e-commerce (tienda_modelo_c.db).

Para ejecutarlo:
1. Asegúrate de tener las librerías: pip install Flask pandas
2. En la terminal, ejecuta: python dashboard_modelo_c.py
3. Abre tu navegador y ve a: http://127.0.0.1:5000
"""

from flask import Flask, render_template_string
import sqlite3
import pandas as pd
from pathlib import Path
import json

# --- CONFIGURACIÓN DE LA APP Y RUTAS ---
app = Flask(__name__)
RUTA_BASE = Path(__file__).parent
DB_MODELO_C = RUTA_BASE / "tienda_modelo_c.db"

# --- FUNCIONES DE CONSULTA A LA BASE DE DATOS ---

def get_db_connection():
    """Crea una conexión a la base de datos con timeout."""
    try:
        conn = sqlite3.connect(DB_MODELO_C, timeout=10)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def obtener_kpis():
    """Obtiene los Indicadores Clave de Rendimiento (KPIs)."""
    conn = get_db_connection()
    if not conn:
        return {"ingresos_totales": 0, "total_pedidos": 0, "total_clientes": 0}

    try:
        ingresos = conn.execute("SELECT SUM(total) FROM pedidos WHERE estado != 'cancelado'").fetchone()[0]
        pedidos = conn.execute("SELECT COUNT(id) FROM pedidos WHERE estado != 'cancelado'").fetchone()[0]
        clientes = conn.execute("SELECT COUNT(id) FROM clientes").fetchone()[0]
    except Exception as e:
        print(f"Error obteniendo KPIs: {e}")
        ingresos, pedidos, clientes = 0, 0, 0
    finally:
        conn.close()

    return {
        "ingresos_totales": round(ingresos or 0, 2),
        "total_pedidos": pedidos or 0,
        "total_clientes": clientes or 0
    }

def obtener_ventas_por_dia():
    """Obtiene los datos de ventas agrupados por día."""
    conn = get_db_connection()
    if not conn:
        return pd.DataFrame()
    
    query = """
    SELECT
        DATE(fecha) as dia,
        SUM(total) as total_ventas
    FROM pedidos
    WHERE estado != 'cancelado'
    GROUP BY dia
    ORDER BY dia;
    """
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        print(f"Error obteniendo ventas: {e}")
        df = pd.DataFrame()
    finally:
        conn.close()
    return df

def obtener_top_clientes():
    """Obtiene el top 5 de clientes por gasto total."""
    conn = get_db_connection()
    if not conn:
        return pd.DataFrame()
        
    query = """
    SELECT
        c.nombre || ' ' || c.apellido AS cliente,
        SUM(p.total) AS gasto_total
    FROM pedidos p
    JOIN clientes c ON p.cliente_id = c.id
    WHERE p.estado != 'cancelado'
    GROUP BY cliente
    ORDER BY gasto_total DESC
    LIMIT 5;
    """
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        print(f"Error obteniendo clientes: {e}")
        df = pd.DataFrame()
    finally:
        conn.close()
    return df

def obtener_top_productos():
    """Obtiene el top 10 de productos más vendidos."""
    conn = get_db_connection()
    if not conn:
        return pd.DataFrame()

    query = """
    SELECT
        p.nombre,
        SUM(lp.cantidad) AS unidades_vendidas
    FROM lineas_pedido lp
    JOIN productos p ON lp.producto_id = p.id
    GROUP BY p.nombre
    ORDER BY unidades_vendidas DESC
    LIMIT 10;
    """
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        print(f"Error obteniendo productos: {e}")
        df = pd.DataFrame()
    finally:
        conn.close()
    return df

def obtener_stock_bajo():
    """Obtiene productos con stock por debajo del mínimo."""
    conn = get_db_connection()
    if not conn:
        return pd.DataFrame()
        
    query = """
    SELECT
        p.nombre,
        i.cantidad_stock,
        i.stock_minimo
    FROM inventario i
    JOIN productos p ON i.producto_id = p.id
    WHERE i.cantidad_stock < i.stock_minimo
    ORDER BY (i.stock_minimo - i.cantidad_stock) DESC;
    """
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        print(f"Error obteniendo stock: {e}")
        df = pd.DataFrame()
    finally:
        conn.close()
    return df

# --- PLANTILLA HTML CON BOOTSTRAP Y CHART.JS ---

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard E-Commerce - Modelo C</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            background-color: #f8f9fa;
        }
        .card {
            border: none;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card-title {
            font-weight: 300;
            color: #6c757d;
        }
        .kpi-value {
            font-size: 2.5rem;
            font-weight: 700;
        }
        .navbar-brand {
            font-weight: 700;
        }
        .chart-container {
            position: relative;
            height: 40vh;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#"><i class="bi bi-bar-chart-line-fill"></i> Dashboard E-Commerce (Modelo C)</a>
        </div>
    </nav>

    <main class="container mt-4">
        <!-- KPIs Principales -->
        <section class="row mb-4">
            <div class="col-md-4">
                <div class="card text-center p-3">
                    <div class="card-body">
                        <h5 class="card-title"><i class="bi bi-currency-dollar"></i> Ingresos Totales</h5>
                        <p class="kpi-value text-success">${{ kpis.ingresos_totales }}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-center p-3">
                    <div class="card-body">
                        <h5 class="card-title"><i class="bi bi-box-seam"></i> Pedidos Realizados</h5>
                        <p class="kpi-value text-primary">{{ kpis.total_pedidos }}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-center p-3">
                    <div class="card-body">
                        <h5 class="card-title"><i class="bi bi-people-fill"></i> Clientes Registrados</h5>
                        <p class="kpi-value text-info">{{ kpis.total_clientes }}</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Gráficos -->
        <section class="row mb-4">
            <div class="col-lg-12">
                <div class="card p-3">
                    <div class="card-body">
                        <h5 class="card-title">Evolución de Ventas Diarias</h5>
                        <div class="chart-container">
                            <canvas id="ventasChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <section class="row mb-4">
            <div class="col-lg-6">
                <div class="card p-3">
                    <div class="card-body">
                        <h5 class="card-title">Top 5 Clientes por Gasto</h5>
                        <div class="chart-container">
                            <canvas id="clientesChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="card p-3">
                    <div class="card-body">
                        <h5 class="card-title">Top 10 Productos Más Vendidos</h5>
                        <div class="chart-container">
                            <canvas id="productosChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Tabla de Alerta de Inventario -->
        <section class="row mb-4">
            <div class="col-12">
                <div class="card p-3">
                    <div class="card-body">
                        <h5 class="card-title text-danger"><i class="bi bi-exclamation-triangle-fill"></i> Alerta de Inventario Bajo</h5>
                        <p class="card-text">Productos cuyo stock actual está por debajo del mínimo requerido.</p>
                        <div class="table-responsive">
                            <table class="table table-hover">
                                <thead class="table-light">
                                    <tr>
                                        <th>Producto</th>
                                        <th class="text-center">Stock Actual</th>
                                        <th class="text-center">Stock Mínimo</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for item in stock_bajo %}
                                    <tr>
                                        <td>{{ item.nombre }}</td>
                                        <td class="text-center text-danger fw-bold">{{ item.cantidad_stock }}</td>
                                        <td class="text-center">{{ item.stock_minimo }}</td>
                                    </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer class="text-center text-muted py-4">
        <p>Dashboard generado con Flask, Pandas, y Chart.js</p>
    </footer>

    <script>
        // Datos inyectados desde Flask de forma segura
        const ventasData = JSON.parse('{{ ventas_data | tojson | safe }}');
        const clientesData = JSON.parse('{{ top_clientes_data | tojson | safe }}');
        const productosData = JSON.parse('{{ top_productos_data | tojson | safe }}');

        // Gráfico de Ventas Diarias (Línea)
        const ventasCtx = document.getElementById('ventasChart').getContext('2d');
        new Chart(ventasCtx, {
            type: 'line',
            data: {
                labels: ventasData.labels,
                datasets: [{
                    label: 'Total Ventas ($)',
                    data: ventasData.values,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    fill: true,
                    tension: 0.1
                }]
            },
            options: { maintainAspectRatio: false }
        });

        // Gráfico de Top Clientes (Barra Horizontal)
        const clientesCtx = document.getElementById('clientesChart').getContext('2d');
        new Chart(clientesCtx, {
            type: 'bar',
            data: {
                labels: clientesData.labels,
                datasets: [{
                    label: 'Gasto Total ($)',
                    data: clientesData.values,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.7)',
                        'rgba(54, 162, 235, 0.7)',
                        'rgba(255, 206, 86, 0.7)',
                        'rgba(75, 192, 192, 0.7)',
                        'rgba(153, 102, 255, 0.7)'
                    ]
                }]
            },
            options: { indexAxis: 'y', maintainAspectRatio: false }
        });

        // Gráfico de Top Productos (Barra Vertical)
        const productosCtx = document.getElementById('productosChart').getContext('2d');
        new Chart(productosCtx, {
            type: 'bar',
            data: {
                labels: productosData.labels,
                datasets: [{
                    label: 'Unidades Vendidas',
                    data: productosData.values,
                    backgroundColor: 'rgba(54, 162, 235, 0.7)'
                }]
            },
            options: { maintainAspectRatio: false }
        });
    </script>
</body>
</html>
"""

# --- RUTAS DE LA APLICACIÓN FLASK ---

@app.route('/')
def dashboard():
    """Renderiza la página principal del dashboard."""
    if not DB_MODELO_C.exists():
        return "<h1>Error: La base de datos 'tienda_modelo_c.db' no existe.</h1><p>Por favor, ejecuta primero el script 'solucion_modelo_c.py' para generarla.</p>", 500

    kpis = obtener_kpis()
    
    # Obtener datos y asegurar que sean listas de Python (no objetos de Pandas/Numpy)
    df_ventas = obtener_ventas_por_dia()
    if not df_ventas.empty:
        ventas_data = {
            "labels": [str(x) for x in df_ventas['dia'].tolist()],
            "values": [float(x) for x in df_ventas['total_ventas'].tolist()]
        }
    else:
        ventas_data = {"labels": [], "values": []}

    df_clientes = obtener_top_clientes()
    if not df_clientes.empty:
        top_clientes_data = {
            "labels": [str(x) for x in df_clientes['cliente'].tolist()],
            "values": [float(x) for x in df_clientes['gasto_total'].tolist()]
        }
    else:
        top_clientes_data = {"labels": [], "values": []}

    df_productos = obtener_top_productos()
    if not df_productos.empty:
        top_productos_data = {
            "labels": [str(x) for x in df_productos['nombre'].tolist()],
            "values": [int(x) for x in df_productos['unidades_vendidas'].tolist()]
        }
    else:
        top_productos_data = {"labels": [], "values": []}

    df_stock = obtener_stock_bajo()
    if not df_stock.empty:
        # Convertir a lista de diccionarios y asegurar tipos nativos
        stock_bajo_data = []
        for _, row in df_stock.iterrows():
            stock_bajo_data.append({
                "nombre": str(row['nombre']),
                "cantidad_stock": int(row['cantidad_stock']),
                "stock_minimo": int(row['stock_minimo'])
            })
    else:
        stock_bajo_data = []

    return render_template_string(
        HTML_TEMPLATE,
        kpis=kpis,
        ventas_data=ventas_data,
        top_clientes_data=top_clientes_data,
        top_productos_data=top_productos_data,
        stock_bajo=stock_bajo_data
    )

# --- PUNTO DE ENTRADA ---

if __name__ == '__main__':
    print("="*50)
    print("🚀 Iniciando Dashboard de E-Commerce con Flask 🚀")
    print(f"Fuente de datos: {DB_MODELO_C.name}")
    print("Para ver el dashboard, abre tu navegador y ve a:")
    print("   👉 http://127.0.0.1:5000")
    print("Para detener el servidor, presiona CTRL+C en esta terminal.")
    print("="*50)
    app.run(debug=True)
