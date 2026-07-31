import streamlit as st

from banco import (
    criar_tabela_plano,
    inserir_alimento,
    listar_pacientes,
    listar_plano
)

criar_tabela_plano()

st.title("🥗 Plano Alimentar")

pacientes = listar_pacientes()

if not pacientes:

    st.warning(
        "Cadastre um paciente primeiro."
    )

else:

    nomes = {}

    for p in pacientes:
        nomes[p[1]] = p[0]

    paciente = st.selectbox(
        "Paciente",
        nomes.keys()
    )

    refeicao = st.selectbox(
        "Refeição",
        [
            "Café da manhã",
            "Lanche da manhã",
            "Almoço",
            "Lanche da tarde",
            "Jantar",
            "Ceia"
        ]
    )

    alimento = st.text_input(
        "Alimento"
    )

    quantidade = st.text_input(
        "Quantidade",
        placeholder="Ex: 100g, 1 unidade"
    )

    calorias = st.number_input(
        "Calorias",
        min_value=0.0
    )

    if st.button("Adicionar alimento"):
        inserir_alimento(
            nomes[paciente],
            refeicao,
            alimento,
            quantidade,
            calorias
        )

        st.success(
            "Alimento adicionado!"
        )

    st.divider()

    st.subheader(
        "📋 Plano atual"
    )

    plano = listar_plano(
        nomes[paciente]
    )

    total = 0

    for item in plano:
        st.write(
            f"""
            **{item[0]}**

            🍽️ {item[1]}

            Quantidade: {item[2]}

            Calorias: {item[3]} kcal
            """
        )

        total += item[3]

        st.divider()

    if plano:
        st.success(
            f"Total diário: {total:.0f} kcal"
        )