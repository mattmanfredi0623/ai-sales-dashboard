import streamlit as st
from core.data_loader import load_data

st.title("📈 Exploratory Data Analysis")

df = load_data()

if df is not None:
    st.subheader("Raw Data")
    st.dataframe(df)

    st.subheader("Column Summary")
    st.write(df.describe(include='all'))
else:
    st.warning("No data available.")