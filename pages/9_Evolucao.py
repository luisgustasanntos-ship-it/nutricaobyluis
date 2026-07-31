import streamlit as st
from datetime import date

import streamlit as st
from banco import listar_pacientes, listar_evolucao, inserir_evolucao
from login import verificar_login

verificar_login()

st.title("📈 Evolução")
from banco import (
    criar_tabela_evolucao,
    inserir_evolucao,
    listar_pacientes,
    listar_evolucao
)


criar_tabela_evolucao()

st.title("📈 Evolução do Paciente")


pacientes = listar_pacientes()


if len(pacientes) == 0:

    st.warning(
        "Cadastre um paciente primeiro."
    )

else:

    nomes = {}

    for p in pacientes:
        nomes[p[1]] = p[0]


    paciente = st.selectbox(
        "Selecione o paciente",
        nomes.keys()
    )


    peso = st.number_input(
        "Peso atual (kg)",
        min_value=1.0
    )


    if st.button("Registrar peso"):

        inserir_evolucao(
            nomes[paciente],
            peso,
            str(date.today())
        )

        st.success(
            "Peso registrado!"
        )


    st.divider()


    st.subheader(
        "Histórico de peso"
    )


    dados = listar_evolucao(
        nomes[paciente]
    )


    if dados:

        st.line_chart(
            {
                "Peso": [
                    x[1]
                    for x in dados
                ]
            }
        )

        for item in dados:
            st.write(
                f"{item[0]} - {item[1]} kg"
            )

    else:

        st.info(
            "Ainda não existem registros."
        )