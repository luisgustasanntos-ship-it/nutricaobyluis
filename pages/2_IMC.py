import streamlit as st

st.title("📏 Calculadora de IMC")

st.write("Calcule seu Índice de Massa Corporal (IMC) e veja a classificação segundo a OMS.")

peso = st.number_input(
    "Peso (kg)",
    min_value=1.0,
    max_value=300.0,
    step=0.1
)

altura = st.number_input(
    "Altura (m)",
    min_value=0.50,
    max_value=2.50,
    step=0.01
)

if st.button("Calcular IMC"):

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Baixo peso"
        mensagem = "É recomendado procurar orientação profissional para avaliação nutricional."
        cor = "warning"

    elif imc < 25:
        classificacao = "Peso adequado (Eutrofia)"
        mensagem = "Parabéns! Seu IMC está dentro da faixa considerada saudável."
        cor = "success"

    elif imc < 30:
        classificacao = "Sobrepeso"
        mensagem = "Há um risco aumentado para algumas doenças. Mudanças no estilo de vida podem ser benéficas."
        cor = "warning"

    elif imc < 35:
        classificacao = "Obesidade Grau I"
        mensagem = "É recomendável acompanhamento com um profissional de saúde."
        cor = "error"

    elif imc < 40:
        classificacao = "Obesidade Grau II"
        mensagem = "Existe um risco elevado para doenças associadas ao excesso de peso."
        cor = "error"

    else:
        classificacao = "Obesidade Grau III"
        mensagem = "Procure acompanhamento médico e nutricional especializado."
        cor = "error"

    peso_min = 18.5 * (altura ** 2)
    peso_max = 24.9 * (altura ** 2)

    st.markdown("---")

    st.metric("IMC", f"{imc:.2f}")

    if cor == "success":
        st.success(classificacao)
    elif cor == "warning":
        st.warning(classificacao)
    else:
        st.error(classificacao)

    st.info(mensagem)

    st.subheader("⚖️ Faixa de peso saudável")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Peso mínimo saudável", f"{peso_min:.1f} kg")

    with col2:
        st.metric("Peso máximo saudável", f"{peso_max:.1f} kg")

    if peso < peso_min:
        st.warning(f"Você está {peso_min - peso:.1f} kg abaixo da faixa saudável.")

    elif peso > peso_max:
        st.warning(f"Você está {peso - peso_max:.1f} kg acima da faixa saudável.")

    else:
        st.success("Seu peso está dentro da faixa saudável.")

    st.markdown("---")

    st.subheader("📋 Classificação da OMS")

    st.table({
        "IMC": [
            "< 18,5",
            "18,5 – 24,9",
            "25,0 – 29,9",
            "30,0 – 34,9",
            "35,0 – 39,9",
            "≥ 40,0"
        ],
        "Classificação": [
            "Baixo peso",
            "Peso adequado",
            "Sobrepeso",
            "Obesidade Grau I",
            "Obesidade Grau II",
            "Obesidade Grau III"
        ]
    })