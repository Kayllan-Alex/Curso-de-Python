primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termos = 1
while termos <= 10:
    print(primeiro_termo)
    primeiro_termo += razao
    termos += 1