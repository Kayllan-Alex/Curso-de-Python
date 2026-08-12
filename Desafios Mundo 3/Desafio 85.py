impares = []
pares = []

for c in range(7):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        pares.append(numero)
        pares.sort()
    else:
        impares.append(numero)
        impares.sort()

print("O valores pares foram:", *pares)
print("O valores impares foram:", *impares)
