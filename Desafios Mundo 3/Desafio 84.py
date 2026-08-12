pessoa_cadastradas = 0
pessoas = []
while True:
    nome_da_pessoa = input("Digite o seu nome: ")
    idade_da_pessoa = int(input("Digite sua idade: "))
    peso_da_pessoa = float(input("Digite seu peso: "))
    pessoas.append([nome_da_pessoa, idade_da_pessoa, peso_da_pessoa])
    pessoa_cadastradas += 1
    while True:
        continuar = input("Você deseja continuar [S] ou [N]: ").upper()
        if continuar in ["S", "N"]:
            break
        else:
            print("Digite apenas [S] ou [N]:")
    if continuar == "N":
        break

print(F"O número total de pessoas cadastradas é de {pessoa_cadastradas}")
for pessoa in pessoas:
    print(f"{pessoa[0]} com {pessoa[1]} anos de idade e pesando {pessoa[2]}")

pessoas.sort(key=lambda pessoa: pessoa[2], reverse=True)
print("A ordem do mais pesado para o mais leve é:")
for pessoa in pessoas:
    print(f"{pessoa[0]}")

pessoas.sort(key=lambda pessoa: pessoa[2])
print("E do mais leve para o mais pesado é:")
for pessoa in pessoas:
    print(f"{pessoa[0]}")