import random
print("Vamos jogar jokenpô!")
escolha = input("Digite Pedra, Papel ou Tesoura: ").lower().replace(" ", "")
opcoes = ["pedra", "papel", "tesoura"]
escolha_da_maquina = random.choice(opcoes)
if escolha not in opcoes:
    print("Escolha inválida!")
elif escolha == escolha_da_maquina:
    print("Jokenpô!")
    print("Empate!")
elif (
    (escolha == "papel" and escolha_da_maquina == "pedra")
    or (escolha == "pedra" and escolha_da_maquina == "tesoura")
    or (escolha == "tesoura" and escolha_da_maquina == "papel")
):
    print("Jokenpô!")
    print(f"Você escolheu {escolha} e eu escolhi {escolha_da_maquina}. Você venceu!")
else:
    print("Jokenpô!")
    print(f"Você escolheu {escolha} e eu escolhi {escolha_da_maquina}. Eu venci!")