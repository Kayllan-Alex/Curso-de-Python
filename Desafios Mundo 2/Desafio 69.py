homens_cadastrados = mulheres_com_menos_de_vinte = maiores_de_idade = pessoas_cadastradas = 0
while True:
    idade = int(input("Digite a idade da pessoa: "))
    while True:
        sexo = input("Digite o sexo da pessoa [F] ou [M]: ").upper()
        if sexo in ["M", "F"]:
            break
        print("Digite apenas F ou M.")
    pessoas_cadastradas += 1
    if idade >= 18:
        maiores_de_idade += 1
    if sexo == "F" and idade < 20:
        mulheres_com_menos_de_vinte += 1
    elif sexo == "M":
        homens_cadastrados += 1
    while True:
        continuar = input("Deseja continuar? [S] ou [N]: ").upper()
        if continuar in ["S", "N"]:
            break
        print("Digite apenas S ou N.")
    if continuar == "N":
        break
print(
    f"{maiores_de_idade} das {pessoas_cadastradas} pessoas cadastradas são maiores de idade"
)
print(f"{homens_cadastrados} das {pessoas_cadastradas} pessoas cadastradas são homens")
print(
    f"{mulheres_com_menos_de_vinte} das {pessoas_cadastradas} pessoas cadastradas são mulheres com menos de vinte"
)