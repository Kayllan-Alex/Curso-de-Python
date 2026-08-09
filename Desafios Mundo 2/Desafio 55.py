mais_pesado = menos_pesado = float(input("Digite o seu peso: "))
for c in range(4):
    peso = float(input("Digite o seu peso: "))
    if peso < menos_pesado:
        menos_pesado = peso
    elif peso > mais_pesado:
        mais_pesado = peso
print(f"A pessoa mais pesada pesa: {mais_pesado}kg")
print(f"A pessoa menos pesada pesa: {menos_pesado}kg")