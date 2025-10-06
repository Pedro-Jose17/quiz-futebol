import streamlit as st

cont_acertos = 0
cont_erros = 0

st.title("Quiz de Futebol")

# Pergunta 1
st.write("1) Qual Seleção ganhou a Copa do Mundo de 2002?")
resposta1 = st.radio("", ["Brasil", "Alemanha", "Itália", "França"])
if st.button("Confirmar Resposta 1"):
    if resposta1 == "Brasil":
        cont_acertos += 1
        st.success("Correto!")
    else:
        cont_erros += 1
        st.error("Errado!")

st.write("-"*30)

# Pergunta 2
st.write("2) Quem é o maior artilheiro de todas as Copas do Mundo?")
resposta2 = st.radio("", ["Ronaldo Fenômeno", "Miroslav Klose", "Pelé", "Lionel Messi"])
if st.button("Confirmar Resposta 2"):
    if resposta2 == "Miroslav Klose":
        cont_acertos += 1
        st.success("Correto!")
    else:
        cont_erros += 1
        st.error("Errado!")

st.write("-"*30)

# Pergunta 3
st.write("3) Qual jogador venceu mais vezes a Bola de Ouro?")
resposta3 = st.radio("", ["Schweinsteiger", "Lionel Messi", "Cristiano Ronaldo", "Pelé"])
if st.button("Confirmar Resposta 3"):
    if resposta3 == "Lionel Messi":
        cont_acertos += 1
        st.success("Correto!")
    else:
        cont_erros += 1
        st.error("Errado!")

st.write("-"*30)

st.write(f"Você acertou {cont_acertos} e errou {cont_erros}")

