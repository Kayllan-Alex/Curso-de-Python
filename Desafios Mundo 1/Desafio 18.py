from math import sin, cos, tan
angulo = float(input("Digite o valor de um ângulo: "))
print(f"O seno de {angulo} é {round(sin(angulo))}", end=", ")
print(f"O cosseno é {round(cos(angulo))}", end=", ")
print(f"E a tangente é {round(tan(angulo))}")