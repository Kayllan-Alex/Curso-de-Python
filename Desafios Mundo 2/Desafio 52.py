numero = int(input("Digite um número: "))
divisor = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisor += 1
if divisor == 2:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")
