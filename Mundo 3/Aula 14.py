teste = []
teste.append("Kayllan")
teste.append(17)
galera = []
galera.append(teste.copy())
teste[0] = "Suelen"
teste[1] = 17
print(teste)
print(galera)

pessoas = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Mária", 45]]
for pessoa in pessoas:
    print(*pessoa)

galera = []
dado = []
total_maior = total_menor = 0
for count in range(3):
    dado.append(input("Digite um nome: "))
    dado.append(int(input("Digite sua idade: ")))
    galera.append(dado.copy())
    dado.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade")
        total_maior += 1
    else:
        print(f"{pessoa[0]} é menor de idade")
        total_menor += 1
print(f"Temos {total_maior} maiores de idade")
print(f"Temos {total_menor} menores de idade")
