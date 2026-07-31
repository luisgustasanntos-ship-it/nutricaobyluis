import streamlit as st

st.set_page_config(
    page_title="NutricaoByLuis",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 NutricaoByLuis")
st.subheader("Sistema de Avaliação Nutricional")

st.markdown("---")

st.markdown("""
Bem-vindo ao **NutricaoByLuis**!

Este sistema reúne ferramentas para auxiliar na avaliação nutricional, cálculo de necessidades energéticas e planejamento alimentar.
""")

st.markdown("## 📋 Ferramentas disponíveis")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📏 **IMC**\n\nCalcule o Índice de Massa Corporal e veja a classificação da OMS.")

with col2:
    st.info("🔥 **TMB**\n\nCalcule a Taxa de Metabolismo Basal.")

with col3:
    st.info("⚡ **GET**\n\nDescubra o Gasto Energético Total com base na atividade física.")

col4, col5 = st.columns(2)

with col4:
    st.info("🍗 **Macronutrientes**\n\nDistribuição de proteínas, carboidratos e gorduras.")

with col5:
    st.info("💧 **Necessidade Hídrica**\n\nCalcule a ingestão diária recomendada de água.")

st.markdown("---")

st.success("👈 Veja ao lado as opções, bixa.")