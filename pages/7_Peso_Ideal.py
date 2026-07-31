import streamlit as st

st.title("⚖️ Peso Ideal")

st.write("Calcule o peso ideal utilizando diferentes métodos.")

sexo = st.selectbox(
    "Sexo",
    ["Masculino", "Feminino"]
)

altura = st.number_input(
    "Altura (cm)",
    min_value=100,
    max_value=250,
    value=170
)

if st.button("Calcular Peso Ideal"):

    altura_pol = altura / 2.54

    # Devine
    if sexo == "Masculino":
        devine = 50 + 2.3 * (altura_pol - 60)
    else:
        devine = 45.5 + 2.3 * (altura_pol - 60)

    # Robinson
    if sexo == "Masculino":
        robinson = 52 + 1.9 * (altura_pol - 60)
    else:
        robinson = 49 + 1.7 * (altura_pol - 60)

    # Hamwi
    if sexo == "Masculino":
        hamwi = 48 + 2.7 * (altura_pol - 60)
    else:
        hamwi = 45.5 + 2.2 * (altura_pol - 60)

    st.subheader("Resultados")

    col1, col2, col3 = st.columns(3)

    col1.metric("Devine", f"{devine:.1f} kg")
    col2.metric("Robinson", f"{robinson:.1f} kg")
    col3.metric("Hamwi", f"{hamwi:.1f} kg")

    st.markdown("---")

    altura_m = altura / 100

    peso_min = 18.5 * altura_m**2
    peso_max = 24.9 * altura_m**2

    st.info(
        f"Faixa saudável pelo IMC: {peso_min:.1f} kg até {peso_max:.1f} kg"
    )