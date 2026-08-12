matriz = []
for c in range(3):
    linha = []
    for i in range(3):
        valor = int(input(f"Digite um valor [{c}, {i}]: "))
        linha.append(valor)
    matriz.append(linha)
for linha in matriz:
    print(linha)
