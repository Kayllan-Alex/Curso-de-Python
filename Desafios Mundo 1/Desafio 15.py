distanciaPercorrida = float(input("Digite quantos km você percorreu com o carro: "))
diasAlugados = float(input("Digite quantos dias você alugou: "))
print(f"O preço total a se pagar é de R${60 * diasAlugados + 0.15 * distanciaPercorrida:.1f}")