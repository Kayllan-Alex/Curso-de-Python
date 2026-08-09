# for c in range(1, 10 + 1):
#     print(c)
# print("Fim")

# c = 1
# while c <= 10:
#     print(c)
#     c += 1
# print("Fim")

# for c in range(3):
#     numero = int(input("Digite um valor: "))
# print("Fim")

# resposta = "sim"
# while resposta == "sim":
#     numero = int(input("Digite um valor: "))
#     resposta = input("Quer continuar? ").lower()
# print("Fim")

numero = 1
pares = impares = 0
while numero != 0:
    numero = int(input("Digite um valor: "))
    if numero != 0:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f"{pares } números eram pares")
print(f"{impares} números eram impares")
