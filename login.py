import streamlit as st

USUARIO = "luis"
SENHA = "1234"


def verificar_login():

    if "logado" not in st.session_state:
        st.session_state["logado"] = False

    if not st.session_state["logado"]:

        st.title("🔐 Área Restrita")

        usuario = st.text_input("Usuário")

        senha = st.text_input(
            "Senha",
            type="password"
        )

        if st.button("Entrar"):

            if usuario == USUARIO and senha == SENHA:

                st.session_state["logado"] = True
                st.success("Login realizado!")
                st.rerun()

            else:

                st.error("Usuário ou senha incorretos")

        st.stop()