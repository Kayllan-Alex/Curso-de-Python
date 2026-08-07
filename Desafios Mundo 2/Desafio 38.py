primeiro_numero = int(input("Digite um valor: "))
segundo_numero = int(input("Digite um segundo valor: "))

if primeiro_numero == segundo_numero:
    print("Os números são iguais!")
elif primeiro_numero > segundo_numero:
    print(f"O número {primeiro_numero} é maior que o número {segundo_numero}.")
else:
    print(f"O número {segundo_numero} é maior que o número {primeiro_numero}.")