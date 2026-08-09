primeiro_valor = int(input("Digite um valor: "))
segundo_valor = int(input("Digite outro valor: "))
terceiro_valor = int(input("Digite mais um valor: "))
quarto_valor = int(input("Digite o último valor: "))
numeros = (primeiro_valor, segundo_valor, terceiro_valor, quarto_valor)

print(f"A quantidade de noves na tupla é de {numeros.count(9)}")
if 3 not in numeros:
    print("Não existe nenhum 3 na tupla.")
else:
    print(f"O primeiro 3 aparece na {numeros.index(3) + 1}ª posição")
print("E os números pares são:", end=" ")
for c in numeros:
    if c % 2 == 0:
        print(c, end=" ")