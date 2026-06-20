import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tablero de Chocolates", page_icon="🍫", layout="wide")
st.title("🍫 Panel de Control de Chocolates")
st.markdown("---")

df = pd.read_csv('app.csv')

# Imprime en la consola de Streamlit las columnas reales para diagnosticar
# Normalizamos los nombres de las columnas pasándolas a mayúsculas para evitar errores
df.columns = [c.strip().upper() for c in df.columns]

# Buscamos de forma flexible las columnas correctas
col_total = [c for c in df.columns if 'TOTAL' in c]
col_ventas = [c for c in df.columns if 'VENTAS' in c or 'QUANTITY' in c or 'CANTIDAD' in c]
col_producto = [c for c in df.columns if 'PRODUCT' in c or 'NOMBRE' in c or 'CHOCOLATE' in c]

# Si encuentra las columnas, arma el tablero. Si no, usa las primeras disponibles para no romperse.
t_col = col_total[0] if col_total else df.columns[-1]
v_col = col_ventas[0] if col_ventas else df.columns[5] if len(df.columns) > 5 else df.columns[0]
p_col = col_producto[0] if col_producto else df.columns[2] if len(df.columns) > 2 else df.columns[0]

# Asegurar que sean valores numéricos para las métricas
df[t_col] = pd.to_numeric(df[t_col], errors='coerce').fillna(0)
df[v_col] = pd.to_numeric(df[v_col], errors='coerce').fillna(0)

total_ventas_dinero = df[t_col].sum()
total_unidades_vendidas = df[v_col].sum()
total_productos_distintos = df[p_col].nunique()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="💰 Facturación Total", value=f"${total_ventas_dinero:,.2f}")
with col2:
    st.metric(label="📦 Unidades Vendidas", value=f"{total_unidades_vendidas:,}")
with col3:
    st.metric(label="🍫 Variedades de Chocolate", value=str(total_productos_distintos))

st.markdown("---")
st.subheader("📈 Rendimiento de Ventas por Producto")

df_grafico = df.groupby(p_col)[t_col].sum().reset_index()
st.bar_chart(data=df_grafico, x=p_col, y=t_col, use_container_width=True)

st.markdown("---")
st.subheader("📋 Registro Completo de Datos")
st.dataframe(df, use_container_width=True)
