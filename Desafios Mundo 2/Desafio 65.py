maior_numero = menor_numero = contador_de_numeros_digitados = soma = 0
resposta = None
while resposta != "S":
    numero = int(input("Digite um número para ser lido: "))
    contador_de_numeros_digitados += 1
    soma += numero
    if contador_de_numeros_digitados == 1:
        maior_numero = menor_numero = numero
    elif numero > maior_numero:
        maior_numero = numero
    elif numero < menor_numero:
        menor_numero = numero
    resposta = input("Deseja encerrar o programa [S] ou [N]: ").upper()
print(f"Média: {soma / contador_de_numeros_digitados}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
