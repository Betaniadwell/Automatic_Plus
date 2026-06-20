import streamlit as st
import pandas as pd

df = pd.read_csv('app.csv')
st.title('🍫 Panel de Control de Chocolates')
st.dataframe(df)
