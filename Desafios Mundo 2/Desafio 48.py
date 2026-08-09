soma = 0
for numero in range(1, 500 + 1):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print(f"A soma dos números ímpares que são múltiplos de 3 é igual a {soma}")
