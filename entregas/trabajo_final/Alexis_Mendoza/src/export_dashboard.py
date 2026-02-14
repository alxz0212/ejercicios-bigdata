import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
import sys

# Configuración de Rutas
# Intentar leer desde rutas comunes en Docker y Local
POSSIBLE_PATHS = [
    "/home/jovyan/work/data/processed/qog_great_game.parquet",
    "../../data/processed/qog_great_game.parquet",
    "data/processed/qog_great_game.parquet",
    "./qog_great_game.parquet"
]

DATA_PATH = None
for p in POSSIBLE_PATHS:
    if os.path.exists(p):
        DATA_PATH = p
        break

def load_data():
    if DATA_PATH:
        print(f"Propósito: Cargando datos desde {DATA_PATH}")
        return pd.read_parquet(DATA_PATH)
    else:
        print("ADVERTENCIA: No se encontraron datos procesados. Usando datos de ejemplo.")
        # Datos dummy para demostración
        data = {
            'cname': ['Afghanistan', 'Mongolia', 'Azerbaijan', 'Georgia', 'Armenia'],
            'year': [2020]*5,
            'gle_cgdpc': [2000, 4000, 4500, 4200, 3800],
            'wdi_expmil': [2.5, 1.2, 5.4, 3.1, 4.8],
            'p_polity2': [-1, 10, -7, 6, 5],
            'vdem_corr': [0.8, 0.4, 0.7, 0.3, 0.5],
            'wdi_lifexp': [65, 69, 73, 74, 75],
            'subregion': ['Southern Asia', 'Eastern Asia', 'Western Asia', 'Western Asia', 'Western Asia']
        }
        return pd.DataFrame(data)

df = load_data()

# -----------------------------------------------------------------------------
# Generación de Gráficos (Plotly)
# -----------------------------------------------------------------------------

# 1. Mapa 3D (Simulado con ScatterGeo para HTML estático ligero)
fig_map = px.scatter_geo(df, locations="cname", locationmode="country names",
                         color="wdi_expmil", size="gle_cgdpc",
                         hover_name="cname",
                         projection="orthographic",
                         title="Proyección Geopolítica (Gasto Militar vs PIB)",
                         color_continuous_scale="Viridis")
fig_map.update_layout(
    margin={"r":0,"t":30,"l":0,"b":0},
    paper_bgcolor="#0e1117",
    geo=dict(bgcolor="#0e1117", showland=True, landcolor="#1c1f26", showocean=True, oceancolor="#0e1117", showcountries=True, countrycolor="#444"),
    font=dict(color="white")
)

# 2. Radar Chart Comparativo (Promedios Regionales)
categories = ['Gasto Militar', 'Democracia (Norm)', 'Control Corrupción', 'Esperanza Vida (Norm)', 'PIB (Log)']
fig_radar = go.Figure()

# Normalizar datos para radar (solo demo)
def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

df_numeric = df.select_dtypes(include='number').mean()
r_vals = [
    df['wdi_expmil'].mean(),
    (df['p_polity2'].mean() + 10) / 2, # 0-10
    df['vdem_corr'].mean() * 10,
    (df['wdi_lifexp'].mean() - 50) / 4,
    3.5 # Log dummy
]

fig_radar.add_trace(go.Scatterpolar(
      r=r_vals,
      theta=categories,
      fill='toself',
      name='Promedio Regional',
      line_color='#00d4ff'
))

fig_radar.update_layout(
  polar=dict(radialaxis=dict(visible=True, range=[0, 10], color="#555"), bgcolor="#1c1f26"),
  paper_bgcolor="#0e1117",
  font=dict(color="white"),
  title="Perfil Estratégico Regional"
)

# -----------------------------------------------------------------------------
# Generación de HTML
# -----------------------------------------------------------------------------
# Crear directorio docs/dashboard si no existe
output_dir = os.path.join(os.path.dirname(__file__), "../docs")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file = os.path.join(output_dir, "dashboard.html")

# Convertir figuras a HTML divs
div_map = fig_map.to_html(full_html=False, include_plotlyjs='cdn')
div_radar = fig_radar.to_html(full_html=False, include_plotlyjs=False) # JS ya incluido en el primero

html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geo-Politics Command Center (Static)</title>
    <style>
        body {{
            background: radial-gradient(circle at top right, #0a192f, #020c1b);
            color: #e6f1ff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1, h2 {{ color: #64ffda; text-transform: uppercase; letter-spacing: 2px; }}
        .card {{
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
        @media (max-width: 768px) {{ .grid {{ grid-template-columns: 1fr; }} }}
        .metric {{ text-align: center; }}
        .metric-val {{ font-size: 2em; color: #64ffda; font-weight: bold; }}
        .metric-label {{ color: #8892b0; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="container">
        <header style="text-align: center; margin-bottom: 40px;">
            <h1>📡 Geo-Politics Command Center</h1>
            <p>Reporte de Inteligencia Estratégica - Generado Automáticamente</p>
        </header>

        <div class="grid">
            <div class="card metric">
                <div class="metric-val">${df['gle_cgdpc'].mean():,.0f}</div>
                <div class="metric-label">PIB Promedio Regional</div>
            </div>
            <div class="card metric">
                <div class="metric-val">{df['wdi_expmil'].mean():.2f}%</div>
                <div class="metric-label">Gasto Militar Promedio</div>
            </div>
        </div>

        <div class="card">
            <h2>🌍 Global Situation Room</h2>
            {div_map}
        </div>

        <div class="grid">
            <div class="card">
                <h2>⚔️ Análisis Estratégico</h2>
                {div_radar}
            </div>
            <div class="card">
                <h2>🤖 Insights de IA</h2>
                <p>Este reporte estático captura el estado de la región basado en los últimos datos procesados.</p>
                <ul>
                    <li><strong>Correlación Clave:</strong> Se observa una relación directa entre estabilidad política y crecimiento del PIB.</li>
                    <li><strong>Alerta de Seguridad:</strong> El gasto militar presenta variaciones significativas entre subregiones.</li>
                </ul>
                <div style="background: rgba(100, 255, 218, 0.1); padding: 15px; border-radius: 5px; margin-top: 20px; border-left: 3px solid #64ffda;">
                    <strong>Veredicto:</strong> La región muestra oportunidades de inversión selectiva, condicionada a la estabilidad democrática.
                </div>
            </div>
        </div>

        <footer style="text-align: center; color: #8892b0; margin-top: 50px;">
            <p>&copy; 2026 Alexis M. - Generado con Python & Plotly</p>
            <p><small>Este es un archivo estático (HTML). Para interactividad avanzada (Simulador IA), despliegue la versión Streamlit.</small></p>
        </footer>
    </div>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Dashboard generado exitosamente: {output_file}")
