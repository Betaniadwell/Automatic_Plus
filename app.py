import streamlit as st
import pandas as pd

# Configuración de la página web
st.set_page_config(page_title="Tablero de Chocolates", page_icon="🍫", layout="wide")

# Título Principal
st.title("🍫 Panel de Control de Chocolates")
st.markdown("---")

# Leer los datos del CSV actualizado
df = pd.read_csv('app.csv')

# --- SECCIÓN 1: TARJETAS DE MÉTRICAS ---
# Usamos los nombres reales de tus columnas que se ven en tu imagen (Ventas y total_)
total_ventas_dinero = df['total_'].sum()
total_unidades_vendidas = df['Ventas'].sum()
total_productos_distintos = df['Product'].nunique()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="💰 Facturación Total", value=f"${total_ventas_dinero:,.2f}")
with col2:
    st.metric(label="📦 Unidades Vendidas", value=f"{total_unidades_vendidas:,}")
with col3:
    st.metric(label="🍫 Variedades de Chocolate", value=str(total_productos_distintos))

st.markdown("---")

# --- SECCIÓN 2: GRÁFICOS INTERACTIVOS ---
st.subheader("📈 Rendimiento de Ventas por Producto")

# Agrupamos las ventas totales por cada tipo de chocolate para armar el gráfico
df_grafico = df.groupby('Product')['total_'].sum().reset_index()

# Mostramos un gráfico de barras nativo de Streamlit
st.bar_chart(data=df_grafico, x='Product', y='total_', use_container_width=True)

st.markdown("---")

# --- SECCIÓN 3: TABLA DE DATOS COMPLETA ---
st.subheader("📋 Registro Completo de Datos")
st.dataframe(df, use_container_width=True)
