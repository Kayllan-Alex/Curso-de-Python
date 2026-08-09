pessoa = ("Kayllan", 17, 79.60)
del(pessoa)
print(pessoa)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(len(c))
print(c.count(5))
print(c.index(5, 1))

lanche = ("Pizza", "Hamburguer", "Açái", "Pudim")

print(sorted(lanche))
print(lanche)

for contador in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[contador]} na posição {contador}")

for position, c in enumerate(lanche):
    print(f"Eu vou comer {c} na posição {position}")

print(lanche[1 : 3 + 1])
lanche[1] = "Refrigerante"