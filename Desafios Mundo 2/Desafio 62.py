primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termos = None
while termos != 0:
    termos = int(input("Quantos termpos você quer mostrar: "))
    for c in range(termos):
        print(primeiro_termo)
        primeiro_termo += razao
print("Programa encerrado.")