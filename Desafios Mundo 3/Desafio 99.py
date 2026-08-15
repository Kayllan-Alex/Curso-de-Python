from time import sleep

def barra():
    print('-' * 50)

def maior(*args):
    barra()
    print('Os valores estão em processo de análise...')
    sleep(1.5)

    maior = None
    for elemento in args:

        print(elemento, end=' ')
        sleep(0.5)
        if maior is None or elemento > maior:
            maior = elemento

    print(f'--> {len(args)} Valores informados...')
    print(f'O maior valor é --> {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
