numero = int(input("Digite um número: "))
fatorial = 1
while numero > 1:
    fatorial *= numero
    numero -= 1
print(f"O fatorial é {fatorial}")