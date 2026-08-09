numero = 0
fibonatti = 1
repeticoes = int(input("Digite quantas repetições: "))
while repeticoes != 0:
    print(numero)
    numero, fibonatti = fibonatti, numero + fibonatti
    repeticoes -= 1