from math import pow, sqrt
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
print(f"A hipotenusa tem o valor igual à {hipotenusa}")