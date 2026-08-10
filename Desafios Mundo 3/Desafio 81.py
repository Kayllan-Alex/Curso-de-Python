numeros = []
contador = contador_do_cinco = 0
while True:
    numero = int(input("Digite um valor para a lista: "))
    numeros.append(numero)
    contador += 1
    if numero == 5:
        contador_do_cinco += 1
    numeros.sort(reverse=True)
    while True:
        continuar = input("Você deseja continuar [S] ou [N]: ").upper()
        if continuar in ["S", "N"]:
            break
        else:
            print("Digite [S] ou [N].")
    if continuar == "N":
        break
print(f"Foram digitados {contador} números")
if contador_do_cinco == 0 or 5 not in numeros:
    print("O número 5 não foi digitado")
else:
    print(f"O número 5 foi digitado {contador_do_cinco} vezes")
print("A ordem decrescente dos números é: ", end=" ")
for numero in numeros:
    print(numero, end=" ")