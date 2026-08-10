valores = []

for cont in range(5):
    valores.append(int(input("Digite um valor: ")))

for chave, item in enumerate(valores):
    print(f"Na posição {chave} encontrei o valor {item}")
print("Cheguei ao final da lista")

a = [2, 3, 4 ,7]
b = a.copy
# b = a[:] Serve do mesmo modo.
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")