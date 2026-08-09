soma_dos_numeros = contador = numero = 0
while numero != 999:
    numero = int(input("Digite um número ou '999' para parar: "))
    if numero != 999:
        soma_dos_numeros += numero
        contador += 1
print(f"Você digitou {contador} números, e a soma entre eles é {soma_dos_numeros}")
