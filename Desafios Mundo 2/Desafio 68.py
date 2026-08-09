from random import randint

win_streak = 0
while True:
    decisao_do_jogador = input("Digite impar ou par: ").lower().replace(" ", "")
    if decisao_do_jogador not in ["impar", "par"]:
        print("Escolha apenas entre impar ou par!")
        continue
    numero = randint(0, 20)
    print(f"O número é {numero}")
    resultado = "par" if numero % 2 == 0 else "impar"
    if decisao_do_jogador == resultado:
        print("Você venceu!")
        win_streak += 1
    else:
        print("Você perdeu!")
        break
print(f"Você ganhou {win_streak} vezes consecutivas!")
