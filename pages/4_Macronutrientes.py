import streamlit as st

st.title("🍗 Distribuição de Macronutrientes")

calorias = st.number_input("Calorias diárias (kcal)", min_value=100)

proteina = st.slider("Proteínas (%)", 10, 50, 25)
carbo = st.slider("Carboidratos (%)", 20, 70, 50)
gordura = st.slider("Gorduras (%)", 10, 40, 25)

total = proteina + carbo + gordura

if total != 100:
    st.warning(f"A soma está em {total}%. Ajuste para 100%.")
else:

    p = (calorias * proteina / 100) / 4
    c = (calorias * carbo / 100) / 4
    g = (calorias * gordura / 100) / 9

    st.success(f"Proteínas: {p:.1f} g")
    st.success(f"Carboidratos: {c:.1f} g")
    st.success(f"Gorduras: {g:.1f} g")