numeros = []
pares = []
impares = []
while True:
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    while True:
        continuar = input("Você deseja continuar [S] ou [N]: ").upper()
        if continuar in ["S", "N"]:
            break
        else:
            print("Digite apenas [S] ou [N].")
    if continuar == "N":
        break
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Todos os números são:", *numeros)
print("Os números pares são:", *pares)
print("Os números impares são:", *impares)