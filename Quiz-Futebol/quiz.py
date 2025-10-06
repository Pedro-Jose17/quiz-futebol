cont_acertos = 0
cont_erros = 0

print("Qual Seleção ganhou a Copa do Mundo de 2002:")
print("1) Brasil")
print("2) Alemanha")
print("3) Itália")
print("4) França")
resposta1 = input("Qual a sua resposta? ")
if resposta1 == "1":
    cont_acertos += 1
else:
    cont_erros += 1

print("-"*30)

print("Quem é o maior artilheiro de todas as Copas do Mundo?")
print("1) Ronaldo Fenômeno")
print("2) Miroslav Klose")
print("3) Pelé")
print("4) Lionel Messi")
resposta2 = input("Qual a sua resposta? ")
if resposta2 == "2":
    cont_acertos += 1
else:
    cont_erros += 1

print("-"*30)

print("Qual jogador venceu mais vezes a Bola de Ouro?")
print("1) Schweinsteiger")
print("2) Lionel Messi")
print("3) Cristiano Ronaldo")
print("4) Pelé")
resposta3 = input("Qual a sua resposta? ")
if resposta3 == "2":
    cont_acertos += 1
else:
    cont_erros += 1

print("-"*30)

print(f"Você acertou {cont_acertos} e errou {cont_erros}")