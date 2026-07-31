import streamlit as st
from banco import criar_tabela, inserir_paciente, listar_pacientes


criar_tabela()

st.title("👤 Cadastro de Pacientes")


nome = st.text_input("Nome completo")

idade = st.number_input(
    "Idade",
    1,
    120
)

sexo = st.selectbox(
    "Sexo",
    ["Masculino", "Feminino"]
)

peso = st.number_input(
    "Peso (kg)",
    min_value=1.0
)

altura = st.number_input(
    "Altura (m)",
    min_value=0.5
)

objetivo = st.selectbox(
    "Objetivo",
    [
        "Emagrecimento",
        "Manutenção",
        "Ganho de massa muscular",
        "Saúde"
    ]
)


if st.button("Salvar paciente"):

    inserir_paciente(
        nome,
        idade,
        sexo,
        peso,
        altura,
        objetivo
    )

    st.success(
        "Paciente salvo no banco de dados!"
    )


st.divider()

st.subheader("📋 Pacientes cadastrados")


pacientes = listar_pacientes()


for paciente in pacientes:

    st.write(
        f"""
        **ID:** {paciente[0]}  
        **Nome:** {paciente[1]}  
        **Idade:** {paciente[2]}  
        **Sexo:** {paciente[3]}  
        **Peso:** {paciente[4]} kg  
        **Altura:** {paciente[5]} m  
        **Objetivo:** {paciente[6]}
        """
    )

    st.divider()