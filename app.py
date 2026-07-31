import streamlit as st


# Configuração da página
st.set_page_config(
    page_title="NutricaoByLuis",
    page_icon="🥗",
    layout="wide"
)


# Cabeçalho
st.title("🥗 NutricaoByLuis")

st.subheader(
    "Sistema para dietinhas do não-nutri ainda"
)


st.write(
    """
    Bem-vindo ao NutricaoByLuis!

    Vamos ficar gostosas até o final do ano.
    """
)


st.divider()


# Apresentação das funções

col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        """
        ### 📊 Avaliação Nutricional

        - IMC
        - TMB
        - GET
        - Macronutrientes
        """
    )



with col3:

    st.markdown(
        """
        ### 🥗 Plano Alimentar

        - Banco de alimentos
        - Cálculo de calorias
        - Organização das refeições
        """
    )


st.divider()


st.info(
    "Use o menu lateral para acessar as opções."
)


st.caption(
    "NutricaoByLuis © 2026"
)