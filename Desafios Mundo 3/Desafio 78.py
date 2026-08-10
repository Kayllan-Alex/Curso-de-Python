maior_numero = menor_numero = None
numeros = []
for item in range(5):
    numeros.append(int(input("Digite valores: ")))
for numero in numeros:
    if maior_numero == None and menor_numero == None:
        maior_numero = menor_numero = numero
    elif numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero
for posicao, numeros_ in enumerate(numeros):
    print(f"O número {numeros_} está na posição {posicao}")
print(f"O maior número é {maior_numero}")
print(f"O menor número é {menor_numero}")

# Forma sem graça de fazer:
# print(f"O maior número é {max(numeros)}")
# print(f"O menor número é {min(numeros)}")