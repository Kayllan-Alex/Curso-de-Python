help()
help(print)
print(input.__doc__)

def dobra(lst):
    """Dobra os valores de uma lista."""
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [9, 3, 6, 1, 8, 4, 27, 7]
dobra(valores)
print(valores)
print(help(dobra))

def somar(a=0, b=0, c=0):
    """Soma os valores A, B e C"""
    s = a + b + c
    print(f"A soma de {a} + {b} + {c} = {s}")

somar()
somar(2, 3)
somar(2, 3, 5)
somar(b=2, c=3)
somar(a=1, b=2, c=3)

def teste():
    x = 8
    print(f"No teste, n vale {n}")
    print(f"No teste, x vale {x}")

n = 4
print(f"No programa principal, n vale {n}")
# print(f"No programa principal, x vale {x}")
teste()

def funcao():
    n1 = 4
    print(f"n1 local = {n1}")

n1 = 2
print(f"n1 global = {n1}")
funcao()

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma de {a} + {b} + {c} = {s}")

somar(3, 2, 5)
somar(2, 2)
somar(6)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f"Os resultados foram {r1}, {r2} e {r3}")