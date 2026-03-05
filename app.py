import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de página
st.set_page_config(page_title="Casa do Vitorino | Intelligence", layout="wide")

# --- INYECCIÓN DE ESTILO CSS (Efecto Glassmorphism & Paleta Douro) ---
st.markdown("""
    <style>
    /* Importar fuente elegante */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Montserrat', sans-serif;
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)), 
                    url("https://images.unsplash.com/photo-1559564389-0730180dd956?q=80&w=2048");
        background-size: cover;
        background-attachment: fixed;
        color: #F5F5F5;
    }

    /* Estilo de las tarjetas (Glassmorphism) */
    div[data-testid="stMetric"] {
        background: rgba(28, 30, 33, 0.75) !important;
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5) !important;
    }

    /* Colores insignia (Oro Viejo) */
    label[data-testid="stMetricLabel"] { color: #F5F5F5 !important; font-weight: 300 !important; letter-spacing: 1px; }
    div[data-testid="stMetricValue"] { color: #D4AF37 !important; font-size: 2.2rem !important; }

    /* Personalización de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: rgba(28, 30, 33, 0.95);
        border-right: 1px solid rgba(212, 175, 55, 0.3);
    }
    
    h1, h2, h3 {
        color: #F5F5F5;
        letter-spacing: 4px;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LÓGICA DE DATOS (Data Engine Python) ---
# Datos integrados (Fallback) basados en tu CSV estratégico
data_raw = {
    "Mes": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
    "Ingresos_Base": [12400, 13950, 15984, 17582, 19762, 24412, 32114, 36628, 26882, 19762, 13950, 16953],
    "GOP_Base": [3900, 5150, 6784, 8082, 9662, 12912, 18914, 22128, 14882, 9262, 5050, 7153]
}
df_base = pd.DataFrame(data_raw)

# Sidebar: Slicers de Escalabilidad
st.sidebar.title("CASA DO VITORINO")
st.sidebar.markdown("---")
n_casas = st.sidebar.select_slider("Escala (Unidades)", options=[1, 2, 3, 4, 5], value=1)
n_habs = st.sidebar.select_slider("Habitaciones / Unidad", options=[3, 4, 5, 6, 7], value=5)

# Cálculo de Escalabilidad & Eficiencia (Fase 4: Economía de Escala 3%)
scale_factor = (n_casas / 1) * (n_habs / 5)
efficiency_bonus = 1 + ((n_casas - 1) * 0.03)

total_ingresos = df_base['Ingresos_Base'].sum() * scale_factor
total_gop = (df_base['GOP_Base'].sum() * scale_factor) * efficiency_bonus
occ_media = 0.55  # Escenario Base [cite: 514]

# --- DASHBOARD LAYOUT (Grid 3x3) ---
st.title("Financial & ESG Dashboard")
st.markdown(f"**Estado del Proyecto:** {'SALUDABLE' if occ_media >= 0.335 else 'ALERTA RIESGO'}")

# Fila 1: KPIs Financieros Core
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Ocupación Media", f"{occ_media*100:.1f} %", delta="Target 50%")
with col2:
    st.metric("ADR (Precio Medio)", "165 €", delta="Premium") # [cite: 475]
with col3:
    st.metric("Ingresos Anuales", f"{total_ingresos:,.0f} €")

# Fila 2: Gráficos Dinámicos (Plotly con colores Douro)
col_gop, col_nps = st.columns([2, 1])

with col_gop:
    fig_gop = go.Figure()
    fig_gop.add_trace(go.Scatter(
        x=df_base['Mes'], 
        y=df_base['GOP_Base'] * scale_factor * efficiency_bonus,
        fill='tozeroy',
        line=dict(color='#D4AF37', width=3),
        fillcolor='rgba(212, 175, 87, 0.2)',
        name="Beneficio (GOP)"
    ))
    fig_gop.update_layout(
        title="Evolución del Beneficio Operativo",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#F5F5F5",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    st.plotly_chart(fig_gop, use_container_width=True)

with col_nps:
    # Gráfico de Satisfacción (NPS)
    st.metric("NPS Score", "94 %", delta="Excelente") # [cite: 537]
    st.markdown("Calidad percibida del Lujo Emocional [cite: 535]")
    # Medidor de estrellas visual (sin emojis)
    progress_nps = 0.94
    st.progress(progress_nps)

# Fila 3: Métricas ESG (Sostenibilidad)
st.markdown("### Sostenibilidad y Compromiso Local")
e1, e2, e3 = st.columns(3)
with e1:
    st.metric("Eficiencia Hídrica", "284 L", delta="-5% s/sector")
    st.caption("Consumo por huésped (Target <300L)")
with e2:
    st.metric("Energía Renovable", "14.5 KWh")
    st.caption("Uso de Aerotermia y Solar")
with e3:
    st.metric("Impacto Local (Km 0)", "85 %", delta="+15% Target") # [cite: 113]
    st.caption("Productos locales del Duero")