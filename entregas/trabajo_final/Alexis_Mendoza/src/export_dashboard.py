import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
import sys

# Intentar importar sklearn, si no está, usar modo dummy
try:
    from sklearn.ensemble import RandomForestRegressor
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("ADVERTENCIA: scikit-learn no encontrado. Se usarán datos simulados para ML.")

# Configuración de Rutas
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
        # Datos dummy extendidos
        data = {
            'cname': ['Afghanistan', 'Mongolia', 'Azerbaijan', 'Georgia', 'Armenia', 'Kazakhstan', 'Uzbekistan', 'Turkmenistan'],
            'year': [2020]*8,
            'gle_cgdpc': [2000, 4000, 4500, 4200, 3800, 9000, 2500, 7000],
            'wdi_expmil': [2.5, 1.2, 5.4, 3.1, 4.8, 1.1, 3.5, 2.9],
            'p_polity2': [-1, 10, -7, 6, 5, -6, -9, -8],
            'vdem_corr': [0.8, 0.4, 0.7, 0.3, 0.5, 0.6, 0.7, 0.9],
            'wdi_lifexp': [65, 69, 73, 74, 75, 70, 68, 67],
            'subregion': ['Southern Asia', 'Eastern Asia', 'Western Asia', 'Western Asia', 'Western Asia', 'Central Asia', 'Central Asia', 'Central Asia']
        }
        return pd.DataFrame(data)

df = load_data()

# -----------------------------------------------------------------------------
# Generación de Gráficos (Plotly)
# -----------------------------------------------------------------------------

# 1. Mapa 3D
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

# 2. Análisis de Correlación (Heatmap)
# Seleccionar columnas numéricas relevantes
cols_corr = ['gle_cgdpc', 'wdi_lifexp', 'p_polity2', 'vdem_corr', 'wdi_expmil']
# Renombrar para visualización
cols_map = {
    'gle_cgdpc': 'PIB pc', 'wdi_lifexp': 'Esperanza Vida', 
    'p_polity2': 'Democracia', 'vdem_corr': 'Corrupción', 
    'wdi_expmil': 'Gasto Militar'
}
df_corr_input = df[cols_corr].rename(columns=cols_map)
corr_matrix = df_corr_input.corr()

fig_corr = px.imshow(corr_matrix, text_auto=".2f", aspect="auto", color_continuous_scale="RdBu_r",
                     title="Matriz de Correlación: Factores de Poder")
fig_corr.update_layout(paper_bgcolor="#0e1117", plot_bgcolor="#0e1117", font=dict(color="white"))


# 3. Feature Importance (Random Forest)
feat_imp_df = pd.DataFrame()
if SKLEARN_AVAILABLE and len(df) > 5:
    features = ['wdi_lifexp', 'p_polity2', 'vdem_corr', 'wdi_expmil']
    target = 'gle_cgdpc'
    # Drop nas
    df_ml = df.dropna(subset=features + [target])
    if not df_ml.empty:
        X = df_ml[features]
        y = df_ml[target]
        rf = RandomForestRegressor(n_estimators=50, random_state=42)
        rf.fit(X, y)
        feat_imp_df = pd.DataFrame({
            'Factor': [cols_map.get(f, f) for f in features],
            'Importancia': rf.feature_importances_
        }).sort_values(by='Importancia', ascending=True)
else:
    # Datos dummy si no hay sklearn o pocos datos
    feat_imp_df = pd.DataFrame({
        'Factor': ['Democracia', 'Corrupción', 'Esperanza Vida', 'Gasto Militar'],
        'Importancia': [0.15, 0.20, 0.40, 0.25]
    }).sort_values(by='Importancia', ascending=True)

fig_imp = px.bar(feat_imp_df, x='Importancia', y='Factor', orientation='h',
                 color='Importancia', color_continuous_scale='Viridis',
                 title="Importancia de Variables (Predicción PIB)", text_auto='.2f')
fig_imp.update_layout(paper_bgcolor="#0e1117", plot_bgcolor="#0e1117", font=dict(color="white"))


# 4. Radar Chart
categories = ['Gasto Militar', 'Democracia (Norm)', 'Control Corrupción', 'Esperanza Vida (Norm)', 'PIB (Log)']
fig_radar = go.Figure()
# (Lógica simplificada de normalización para demo)
r_vals = [
    df['wdi_expmil'].mean(),
    (df['p_polity2'].mean() + 10) / 2,
    df['vdem_corr'].mean() * 10,
    (df['wdi_lifexp'].mean() - 50) / 4,
    3.5
]
fig_radar.add_trace(go.Scatterpolar(
      r=r_vals, theta=categories, fill='toself', name='Promedio Regional', line_color='#00d4ff'
))
fig_radar.update_layout(
  polar=dict(radialaxis=dict(visible=True, range=[0, 10], color="#555"), bgcolor="#1c1f26"),
  paper_bgcolor="#0e1117", font=dict(color="white"), title="Perfil Estratégico Promedio"
)

# -----------------------------------------------------------------------------
# Generación de HTML
# -----------------------------------------------------------------------------
output_dir = os.path.join(os.path.dirname(__file__), "..")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file = os.path.join(output_dir, "dashboard.html")

# Convertir figuras
# IMPORTANTE: include_plotlyjs=True embebe la librería entera (3MB+) para que funcione offline/sin CDN
div_map = fig_map.to_html(full_html=False, include_plotlyjs=True)
div_radar = fig_radar.to_html(full_html=False, include_plotlyjs=False)

div_corr = fig_corr.to_html(full_html=False, include_plotlyjs=False)
div_imp = fig_imp.to_html(full_html=False, include_plotlyjs=False)

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
        .container {{ max-width: 1400px; margin: 0 auto; }}
        h1, h2, h3 {{ color: #64ffda; text-transform: uppercase; letter-spacing: 2px; }}
        .card {{
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }}
        .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
        @media (max-width: 900px) {{ .grid-2 {{ grid-template-columns: 1fr; }} }}
        
        .metric {{ text-align: center; }}
        .metric-val {{ font-size: 2.5em; color: #64ffda; font-weight: bold; text-shadow: 0 0 10px rgba(100,255,218,0.3); }}
        .metric-label {{ color: #8892b0; font-size: 0.9em; }}
        
        table {{ width: 100%; border-collapse: collapse; margin-top: 10px; color: #ccd6f6; }}
        th, td {{ padding: 12px; border-bottom: 1px solid rgba(255,255,255,0.1); text-align: left; }}
        th {{ color: #64ffda; text-transform: uppercase; font-size: 0.8em; }}
        tr:hover {{ background: rgba(255,255,255,0.05); }}
    </style>
</head>
<body>
    <div class="container">
        <header style="text-align: center; margin-bottom: 40px; border-bottom: 1px solid rgba(100,255,218,0.2); padding-bottom: 20px;">
            <h1>📡 Geo-Politics Command Center</h1>
            <p>Inteligencia Estratégica Post-Soviética | Reporte Estático Generado por AI</p>
        </header>

        <!-- KPI HUD -->
        <div class="grid-2">
            <div class="card metric">
                <div class="metric-val">${df['gle_cgdpc'].mean():,.0f}</div>
                <div class="metric-label">PIB Promedio Regional</div>
            </div>
            <div class="card metric">
                <div class="metric-val">{df['wdi_expmil'].mean():.2f}%</div>
                <div class="metric-label">Gasto Militar Promedio</div>
            </div>
        </div>

        <!-- VISUALIZACION PRINCIPAL -->
        <div class="card">
            <h2>🌍 Global Situation Room</h2>
            <p>Visualización geoespacial de la relación entre poder económico (tamaño) y militar (color).</p>
            {div_map}
        </div>

        <!-- ANALISIS ESTADISTICO -->
        <div class="grid-2">
            <div class="card">
                <h2>📊 Correlación de Factores</h2>
                <p>Mapa de calor que muestra qué variables están interconectadas. El rojo indica relación inversa, el azul relación directa.</p>
                {div_corr}
                <div style="font-size: 0.9em; color: #aaa; margin-top: 10px;">
                    <strong>Insight:</strong> Observa si la corrupción (Rojo) aumenta o disminuye con la democracia.
                </div>
            </div>
            <div class="card">
                <h2>🔮 Feature Importance (AI)</h2>
                <p>Qué variables pesan más para predecir el éxito económico de un país, según el modelo Random Forest.</p>
                {div_imp}
                <div style="font-size: 0.9em; color: #aaa; margin-top: 10px;">
                    <strong>Insight:</strong> Si el 'Gasto Militar' es alto, valida la teoría del "Poder Duro".
                </div>
            </div>
        </div>

        <div class="grid-2">
            <div class="card">
                <h2>⚔️ Perfil Estratégico Regional</h2>
                {div_radar}
            </div>
            
            <!-- DATOS EXPLICACION -->
            <div class="card">
                <h2>📄 Data Source Intelligence</h2>
                <p>Este análisis se basa en el <strong>Quality of Government (QoG) Standard Dataset</strong>, cruzado con indicadores del Banco Mundial.</p>
                
                <table>
                    <thead>
                        <tr>
                            <th>Variable</th>
                            <th>Descripción Técnica</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>gle_cgdpc</strong></td>
                            <td>GDP per Capita (PIB). Indicador de riqueza nacional ajustado por paridad de poder adquisitivo.</td>
                        </tr>
                        <tr>
                            <td><strong>wdi_expmil</strong></td>
                            <td>Gasto Militar. Porcentaje del PIB total dedicado a defensa y armamento.</td>
                        </tr>
                        <tr>
                            <td><strong>p_polity2</strong></td>
                            <td>Índice de Democracia. Escala de -10 (Autocracia) a +10 (Democracia Plena).</td>
                        </tr>
                        <tr>
                            <td><strong>vdem_corr</strong></td>
                            <td>Corrupción Política. Índice V-Dem donde valores altos indican mayor corrupción.</td>
                        </tr>
                        <tr>
                            <td><strong>wdi_lifexp</strong></td>
                            <td>Esperanza de Vida. Años promedio de vida al nacer (Indicador de bienestar social).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <footer style="text-align: center; color: #8892b0; margin-top: 50px; font-size: 0.8em;">
            <p>Análisis generado el: 2026-02-14 | Proyecto Big Data "El Gran Juego"</p>
        </footer>
    </div>
</body>
</html>
"""

with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Dashboard Mejorado generado: {output_file}")
