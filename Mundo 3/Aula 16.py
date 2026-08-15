def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma de A + B = {s}")

soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(a = 2, b = 5)
soma(b = 2, a = 5)


def contador(*numeros):
    print(numeros)

contador(1, 2, 3)
contador(4, 2)
contador(5, 2, 7, 1)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [9, 3, 6, 1, 8, 4, 27, 7]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for n in valores:
        s += n
    print(f"A soma dos valores {valores} é {s}")

soma(5, 2)