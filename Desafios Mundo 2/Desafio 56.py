media_de_idade = mulheres_com_menos_de_vinta = maior_idade = 0
nome_do_mais_velho = None
for i in range(4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo [F] ou [M]: ").upper()
    media_de_idade += idade
    if idade > maior_idade and sexo == "M":
        maior_idade = idade
        nome_do_mais_velho = nome
    elif idade < 20 and sexo == "F":
        mulheres_com_menos_de_vinta += 1
print(f"A média de idade do grupo é {media_de_idade / 4}")
print(
    f"O nome do mais velho é {nome_do_mais_velho}"
    if nome_do_mais_velho is not None
    else "Você não cadastrou nenhum homem."
)
print(f"E tem {mulheres_com_menos_de_vinta} mulheres com menos de 20 anos.")
