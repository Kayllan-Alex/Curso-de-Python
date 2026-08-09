quantidade_de_valores = soma_dos_valores = 0
while True:
    numero = int(input("Digite um valor [999] para encerrar: "))
    if numero == 999:
        break
    soma_dos_valores += numero
    quantidade_de_valores += 1
print(f"A soma dos {quantidade_de_valores} valores foi de {soma_dos_valores}!")