import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Configuración de página
st.set_page_config(page_title="Casa do Vitorino | Intelligence", layout="wide")

# 2. INYECCIÓN DE CSS AVANZADO (El alma del diseño)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');

    /* Fondo de pantalla con fotografía del Alto Douro */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)), 
                    url("https://images.unsplash.com/photo-1559564389-0730180dd956?q=80&w=2048");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Contenedor principal y fuentes */
    html, body, [data-testid="stAppViewContainer"], .main {
        font-family: 'Montserrat', sans-serif;
        color: #F5F5F5;
    }

    /* Tarjetas con Efecto Glassmorphism */
    div[data-testid="stMetric"] {
        background: rgba(28, 30, 33, 0.75) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 15px !important;
        padding: 25px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5) !important;
        transition: transform 0.3s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #D4AF37 !important;
    }

    /* Colores de las métricas (Oro Viejo) */
    label[data-testid="stMetricLabel"] { 
        color: #F5F5F5 !important; 
        font-weight: 300 !important; 
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    div[data-testid="stMetricValue"] { 
        color: #D4AF37 !important; 
        font-size: 2.5rem !important;
        font-weight: 600 !important;
    }

    /* Personalización de Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(18, 18, 18, 0.98);
        border-right: 1px solid #D4AF37;
    }

    /* Títulos con tracking expandido */
    h1, h2 {
        letter-spacing: 6px !important;
        text-transform: uppercase;
        color: #F5F5F5;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* Ocultar elementos innecesarios de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE NEGOCIO (Recalculada)
st.sidebar.title("CASA DO VITORINO")
st.sidebar.markdown("---")
n_casas = st.sidebar.select_slider("Unidades", options=[1, 2, 3, 4, 5], value=1)
n_habs = st.sidebar.select_slider("Habitaciones / Unidad", options=[3, 4, 5, 6, 7], value=5)

# Datos Mock para visualización (Simulando tu CSV)
scale_factor = (n_casas / 1) * (n_habs / 5)
efficiency = 1 + ((n_casas - 1) * 0.03) # Bono eficiencia 3%

# 4. DASHBOARD ESTRUCTURADO
st.title("Strategic Intelligence")
st.write(f"PROYECCIÓN PARA {n_casas} UNIDAD(ES) CON {n_habs} HABITACIONES")

# Fila 1: KPIs Principales
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Ocupación Target", "52 %", delta="Saludable")
with c2:
    st.metric("RevPAR Proyectado", f"{162 * efficiency:,.1f} €")
with c3:
    st.metric("GOP Anual Estimado", f"{145800 * scale_factor * efficiency:,.0f} €")

st.markdown("---")

# Fila 2: Gráfico de Tendencia (Plotly estilizado)
col_chart, col_esg = st.columns([2, 1])

with col_chart:
    months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    values = [12, 15, 18, 22, 28, 35, 45, 48, 38, 28, 18, 15]
    
    fig = go.Figure(go.Scatter(
        x=months, y=[v * scale_factor for v in values],
        fill='tozeroy', line_color='#D4AF37', fillcolor='rgba(212, 175, 55, 0.1)'
    ))
    fig.update_layout(
        title="Curva de Ingresos Proyectada",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#F5F5F5",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    st.plotly_chart(fig, use_container_width=True)

with col_esg:
    st.subheader("Compromiso ESG")
    st.write("Eficiencia Hídrica")
    st.progress(70) # Representación visual
    st.caption("Consumo actual: 284L (Objetivo <300L)")
    
    st.write("Suministro Km 0")
    st.progress(85)
    st.caption("Vinculación local: 85% (Objetivo >80%)")

# Footer Sutil
st.markdown("<br><br><center><small>CASA DO VITORINO | PORTO & DOURO</small></center>", unsafe_allow_html=True)