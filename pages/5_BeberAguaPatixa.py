import streamlit as st

st.title("💧 Necessidade Hídrica")

peso = st.number_input("Peso (kg)", min_value=1.0)

if st.button("Calcular Água"):

    agua = peso * 35

    st.success(f"Ingestão diária recomendada: {agua:.0f} mL")
    st.info(f"Aproximadamente {agua/1000:.2f} litros por dia.")