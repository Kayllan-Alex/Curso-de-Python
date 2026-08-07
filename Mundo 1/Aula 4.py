from math import sqrt, ceil, floor
numero = float(input("Digite um número: "))
raizDoNumero = sqrt(numero)
print(f"A raiz quadrada de {numero} é {ceil(raizDoNumero):.1f}")
print(f"A raiz quadrada de {numero} é {floor(raizDoNumero):.1f}")