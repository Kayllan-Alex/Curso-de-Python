for c in range(0, 10, 2):
    print(c)
for c in range(6+1, 0, -1):
    print(c)
print("Fim")

numero = int(input("Digite um número: "))
for c in range(0, numero+1):
    print(c)
    
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite os passos: "))
for c in range(inicio, fim+1, passo):
    print(c)

soma = 0
for c in range(0, 3):
    numero = int(input("Digite um valor: "))
    soma += numero
print(f"A soma de todos os valores foi {soma}")