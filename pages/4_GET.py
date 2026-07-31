import streamlit as st

st.title("⚡ Gasto Energético Total (GET)")

st.subheader("Calculadora de GET")

idade = st.number_input("Idade", 1, 120)

peso = st.number_input("Peso (kg)", 1.0)

altura = st.number_input("Altura (cm)", 50.0)

sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])

atividade = st.selectbox(
    "Nível de atividade física",
    [
        "Sedentário",
        "Levemente ativo",
        "Moderadamente ativo",
        "Muito ativo",
        "Extremamente ativo"
    ]
)

if st.button("Calcular GET"):

    if sexo == "Masculino":
        tmb = 10 * peso + 6.25 * altura - 5 * idade + 5
    else:
        tmb = 10 * peso + 6.25 * altura - 5 * idade - 161

    fatores = {
        "Sedentário": 1.2,
        "Levemente ativo": 1.375,
        "Moderadamente ativo": 1.55,
        "Muito ativo": 1.725,
        "Extremamente ativo": 1.9
    }

    fator = fatores[atividade]
    get = tmb * fator

    st.success(f"TMB: {tmb:.0f} kcal/dia")
    st.success(f"GET: {get:.0f} kcal/dia")