contador = 1
while True:
    print(contador, end=" ")
    contador += 1
print("Acabou")

numero = soma = 0
while numero != 999:
    numero = int(input("Digite um número: "))
    if numero != 999:
        soma += numero
print(f"A soma vale {soma}")

numero = soma = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == 999:
        break
    soma += numero
print(f"A soma vale {soma}")