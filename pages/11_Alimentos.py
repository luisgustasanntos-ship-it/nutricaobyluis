import streamlit as st

from banco import (
    criar_tabela_alimentos,
    inserir_alimento_base,
    listar_alimentos
)


criar_tabela_alimentos()


st.title("🍎 Banco de Alimentos")


nome = st.text_input("Nome do alimento")

porcao = st.text_input(
    "Porção",
    placeholder="Ex: 1 unidade (50g)"
)

calorias = st.number_input(
    "Calorias (kcal)"
)

proteina = st.number_input(
    "Proteína (g)"
)

carboidrato = st.number_input(
    "Carboidrato (g)"
)

gordura = st.number_input(
    "Gordura (g)"
)


if st.button("Salvar alimento"):

    inserir_alimento_base(
        nome,
        porcao,
        calorias,
        proteina,
        carboidrato,
        gordura
    )

    st.success(
        "Alimento salvo!"
    )


st.divider()

st.subheader("📋 Alimentos cadastrados")


for alimento in listar_alimentos():

    st.write(
        f"""
        🍽️ **{alimento[1]}**

        Porção: {alimento[2]}

        🔥 {alimento[3]} kcal

        🥩 Proteína: {alimento[4]}g

        🍚 Carboidrato: {alimento[5]}g

        🧈 Gordura: {alimento[6]}g
        """
    )

    st.divider()