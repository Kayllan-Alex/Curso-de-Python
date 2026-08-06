primeiroNumero = int(input("Digite um valor: "))
segundoNumero = int(input("Digite um valor: "))
soma = segundoNumero + primeiroNumero
# print("A soma entre" , primeiroNumero , "e" , segundoNumero , "vale" , soma) Modo sem formatação
# print("A soma entre {} e {} vale {}".format(primeiroNumero, segundoNumero, soma)) Formatação antiga
print(f"A soma entre {segundoNumero} e {primeiroNumero} vale {soma}")