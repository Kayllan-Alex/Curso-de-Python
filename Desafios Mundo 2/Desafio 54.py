maiores_de_idade = menores_de_idade = 0
for c in range(7):
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        maiores_de_idade += 1
    else:
        menores_de_idade += 1
print(f"Das 7 pessoas, {menores_de_idade} são menores de idade.")
print(f"E {maiores_de_idade} são maiores de idade.")