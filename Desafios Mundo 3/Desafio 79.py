numeros = []
while True:
    numero = int(input("Digite um número: "))
    if numero in numeros:
        print("Esse número já está na lista!")
    numeros.append(numero)
    while True:
        continuar = input("Quer continuar [S] ou [N]: ").upper()
        if continuar in ["S", "N"]:
            break
    if continuar == "N":
        break
if numeros != []:
    print("Os valores digitados são:", end=" ")
    numeros.sort()
    for c in numeros:
        print(c, end=" ")
else:
    print("Você não digitou nenhum número.")