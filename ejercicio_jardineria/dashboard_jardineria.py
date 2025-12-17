"""
Dashboard Interactivo para la Base de Datos de Jardinería.
Visualiza KPIs, mapas de clientes y rendimiento de ventas.

Ejecutar con:
streamlit run ejercicio_jardineria/dashboard_jardineria.py
"""

import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Jardinería Analytics",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS ---
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }
    .metric-card {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        text-align: center;
    }
    h1, h2, h3 {
        color: #4CAF50 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- RUTAS ---
DIRECTORIO_SCRIPT = Path(__file__).parent.resolve()
RUTA_DB = DIRECTORIO_SCRIPT / "jardineria.db"

# --- FUNCIONES DE CARGA ---
@st.cache_data
def cargar_datos(query):
    if not RUTA_DB.exists():
        return None
    with sqlite3.connect(RUTA_DB) as conn:
        return pd.read_sql_query(query, conn)

# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1598/1598196.png", width=100)
st.sidebar.title("🌿 Menú Principal")
opcion = st.sidebar.radio("Navegación", ["Visión General", "Análisis de Ventas", "Mapa de Clientes", "Recursos Humanos"])
st.sidebar.divider()
st.sidebar.info("Dashboard desarrollado con Streamlit y Python.")

# --- PÁGINA 1: VISIÓN GENERAL ---
if opcion == "Visión General":
    st.title("📊 Visión General del Negocio")
    
    # KPIs Principales
    col1, col2, col3, col4 = st.columns(4)
    
    # Consultas para KPIs
    df_clientes = cargar_datos("SELECT COUNT(*) as total FROM cliente")
    df_pedidos = cargar_datos("SELECT COUNT(*) as total FROM pedido")
    df_pagos = cargar_datos("SELECT SUM(total) as total FROM pago")
    df_prods = cargar_datos("SELECT COUNT(*) as total FROM producto")
    
    total_clientes = df_clientes.iloc[0]['total']
    total_pedidos = df_pedidos.iloc[0]['total']
    total_ingresos = df_pagos.iloc[0]['total']
    total_productos = df_prods.iloc[0]['total']
    
    col1.metric("Clientes Activos", total_clientes, "Global")
    col2.metric("Pedidos Totales", total_pedidos, "+5 hoy")
    col3.metric("Ingresos Totales", f"${total_ingresos:,.2f}", "+12%")
    col4.metric("Productos en Catálogo", total_productos, "Stock")
    
    st.divider()
    
    # Gráfico de Estado de Pedidos
    col_graf1, col_graf2 = st.columns(2)
    
    with col_graf1:
        st.subheader("📦 Estado de los Pedidos")
        df_estados = cargar_datos("SELECT estado, COUNT(*) as cantidad FROM pedido GROUP BY estado")
        fig_pie = px.pie(
            df_estados, 
            values='cantidad', 
            names='estado', 
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Greens_r
        )
        fig_pie.update_layout(template="plotly_dark")
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_graf2:
        st.subheader("💳 Métodos de Pago")
        df_formas = cargar_datos("SELECT forma_pago, COUNT(*) as cantidad FROM pago GROUP BY forma_pago")
        fig_bar = px.bar(
            df_formas, 
            x='forma_pago', 
            y='cantidad', 
            color='cantidad',
            color_continuous_scale='Greens'
        )
        fig_bar.update_layout(template="plotly_dark", xaxis_title="Método", yaxis_title="Transacciones")
        st.plotly_chart(fig_bar, use_container_width=True)

# --- PÁGINA 2: ANÁLISIS DE VENTAS ---
elif opcion == "Análisis de Ventas":
    st.title("💰 Análisis de Ventas y Productos")
    
    # Ventas por Gama
    st.subheader("🏆 Top Gamas de Productos (Por Precio Promedio)")
    query_gama = """
    SELECT gama, AVG(precio_venta) as precio_promedio, COUNT(*) as cantidad_productos
    FROM producto
    GROUP BY gama
    ORDER BY precio_promedio DESC
    """
    df_gama = cargar_datos(query_gama)
    
    fig_gama = px.bar(
        df_gama,
        x='precio_promedio',
        y='gama',
        orientation='h',
        color='precio_promedio',
        text='precio_promedio',
        color_continuous_scale='Viridis',
        labels={'precio_promedio': 'Precio Promedio ($)', 'gama': 'Gama'}
    )
    fig_gama.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
    fig_gama.update_layout(template="plotly_dark", height=500)
    st.plotly_chart(fig_gama, use_container_width=True)
    
    # Detalle de Productos
    st.subheader("🔎 Explorador de Productos")
    gama_filter = st.selectbox("Filtrar por Gama:", ["Todas"] + df_gama['gama'].tolist())
    
    query_prod = "SELECT codigo_producto, nombre, gama, precio_venta, cantidad_en_stock FROM producto"
    if gama_filter != "Todas":
        query_prod += f" WHERE gama = '{gama_filter}'"
        
    df_prod = cargar_datos(query_prod)
    st.dataframe(df_prod, use_container_width=True)

# --- PÁGINA 3: MAPA DE CLIENTES ---
elif opcion == "Mapa de Clientes":
    st.title("🌍 Distribución Geográfica de Clientes")
    st.info("Nota: Como los datos son ficticios (Faker), simularemos coordenadas geográficas aproximadas para visualizar el mapa.")
    
    df_geo = cargar_datos("SELECT ciudad, pais, COUNT(*) as clientes FROM cliente GROUP BY ciudad, pais")
    
    # Simulación de coordenadas (En un caso real, tendrías lat/lon en la BD)
    # Aquí usamos un truco visual: dispersión aleatoria sobre un mapa base
    import numpy as np
    
    # Coordenadas base (Centro de Europa/España aprox)
    lat_base = 40.0
    lon_base = -3.0
    
    # Generar dispersión
    df_geo['lat'] = lat_base + np.random.normal(0, 10, len(df_geo))
    df_geo['lon'] = lon_base + np.random.normal(0, 15, len(df_geo))
    
    fig_map = px.scatter_mapbox(
        df_geo,
        lat="lat",
        lon="lon",
        hover_name="ciudad",
        hover_data=["pais", "clientes"],
        color="clientes",
        size="clientes",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=50,
        zoom=2,
        mapbox_style="carto-darkmatter"
    )
    fig_map.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)
    
    st.markdown("### 📍 Detalle por País")
    df_pais = cargar_datos("SELECT pais, COUNT(*) as total FROM cliente GROUP BY pais ORDER BY total DESC")
    st.bar_chart(df_pais.set_index('pais'))

# --- PÁGINA 4: RECURSOS HUMANOS ---
elif opcion == "Recursos Humanos":
    st.title("👥 Gestión de Talento")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Organigrama de Ventas (Top Empleados)")
        # Empleados con más clientes asignados
        query_emp = """
        SELECT e.nombre || ' ' || e.apellido1 as empleado, e.puesto, COUNT(c.codigo_cliente) as clientes_asignados
        FROM empleado e
        LEFT JOIN cliente c ON e.codigo_empleado = c.codigo_empleado_rep_ventas
        GROUP BY e.codigo_empleado
        ORDER BY clientes_asignados DESC
        LIMIT 10
        """
        df_emp = cargar_datos(query_emp)
        
        fig_emp = px.bar(
            df_emp,
            x='empleado',
            y='clientes_asignados',
            color='clientes_asignados',
            title="Empleados con mayor cartera de clientes",
            color_continuous_scale='Teal'
        )
        fig_emp.update_layout(template="plotly_dark")
        st.plotly_chart(fig_emp, use_container_width=True)
        
    with col2:
        st.subheader("Distribución por Oficina")
        df_oficina = cargar_datos("""
        SELECT o.ciudad, COUNT(e.codigo_empleado) as personal
        FROM oficina o
        JOIN empleado e ON o.codigo_oficina = e.codigo_oficina
        GROUP BY o.ciudad
        """)
        st.dataframe(df_oficina, use_container_width=True)
        
        fig_sun = px.sunburst(
            df_oficina,
            path=['ciudad'],
            values='personal',
            color='personal',
            title="Personal por Sede"
        )
        st.plotly_chart(fig_sun, use_container_width=True)

else:
    st.error("Opción no válida")
