from random import randint

menor_numero = maior_numero = 0
numeros = tuple(randint(0, 100) for c in range(5))
for c in numeros:
    if menor_numero == 0 and maior_numero == 0:
        maior_numero = menor_numero = c
    if maior_numero < c:
        maior_numero = c
    elif menor_numero > c:
        menor_numero = c
    print(c, end=" ")
print(f"\nO maior número é {maior_numero} e o menor é {menor_numero}")