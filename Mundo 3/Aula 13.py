numero = [2, 5, 9, 1]
numero[2] = 3
numero.append(7)
numero.sort(reverse=True)
numero.insert(2, 2)
if 5 in numero:
    numero.remove(5)
else:
    print("Não achei o número 5.")
# numero.pop(2)
print(numero)
print(f"Essa lista tem {len(numero)} elementos.")