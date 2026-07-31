import streamlit as st

st.title("🔥 Calculadora de Calorias")

idade = st.number_input("Idade", 1, 120)

peso = st.number_input("Peso (kg)", 1.0)

altura = st.number_input("Altura (cm)", 50.0)

sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])

if st.button("Calcular"):
    if sexo == "Masculino":
        tmb = 10 * peso + 6.25 * altura - 5 * idade + 5
    else:
        tmb = 10 * peso + 6.25 * altura - 5 * idade - 161

    st.success(f"Sua Taxa Basal é {tmb:.0f} kcal/dia")