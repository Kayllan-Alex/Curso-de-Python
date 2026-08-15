from random import randint
numeros = []


def sorteia():
    print('Sorteando 5 valores para lista --> ', end='')
    for cont in range(5):
        valorSorteado = randint(1, 10)
        numeros.append(valorSorteado)
        print(f'{valorSorteado}', end=' ')
    print('Prontinho...')


def soma_par(lista_valores):
    par = 0
    for valor in lista_valores:
        if valor % 2 == 0:
            par += valor

    print(f'A soma de todos valores pares de: {lista_valores}, é igual a --> {par}')


sorteia()
soma_par(numeros)
