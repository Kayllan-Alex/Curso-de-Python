numero_pensado = 5
numero_escolhido = int(input("O computador pensou em um número tente acertar: "))
if numero_escolhido == numero_pensado:
    print(f"Você venceu! o computador pensou no número {numero_pensado}")
else:
    print(f"Você perdeu! boa sorte da proxima vez.")