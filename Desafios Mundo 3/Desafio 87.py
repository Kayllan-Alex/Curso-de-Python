matriz = []
soma_dos_pares = maior_valor = soma_da_coluna = 0
for c in range(3):
    linha = []
    for i in range(3):
        valor = int(input(f"Digite um valor [{c}, {i}]: "))
        if valor % 2 == 0:
            soma_dos_pares += valor

        linha.append(valor)
    matriz.append(linha)
for linha in matriz:
    soma_da_coluna += linha[2]
print(
    f"A soma dos pares é {soma_dos_pares}, "
    f"a soma da terceira coluna é {soma_da_coluna} "
    f"e o maior valor da segunda linha é {max(matriz[1])}"
)