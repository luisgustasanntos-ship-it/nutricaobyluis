import streamlit as st

st.set_page_config(
    page_title="NutricaoByLuis",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 NutricaoByLuis")
st.subheader("Sua saúde começa pela alimentação.")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("""
    Bem-vindo ao **NutricaoByLuis**!

    Aqui você poderá:

    ✅ Calcular seu IMC

    ✅ Descobrir seu gasto calórico diário

    ✅ Calcular macronutrientes

    ✅ Acompanhar sua evolução

    ✅ Receber orientações nutricionais
    """)

with col2:
    st.image(
        "https://images.unsplash.com/photo-1490645935967-10de6ba17061",
        use_container_width=True
    )

st.markdown("---")

st.success("Escolha uma ferramenta no menu quando elas forem adicionadas.")