from time import sleep


# Função para contagem personalizada
def contador(inicio, fim, passo):
    print('-' * 35)
    passo = abs(passo) if passo != 0 else 1  # Definindo o passo como valor absoluto (Deixa sinal positivo), e caso seja zero, receba 1
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')

    sleep(1.5)

    if inicio < fim:
        for cont in range(inicio, fim + 1, passo):
            print(cont, end=' ')
            sleep(0.3)
    elif inicio > fim:
        for cont in range(inicio, fim - 1, -passo):
            print(cont, end=' ')
            sleep(0.3)
    print('Prontinho...')


contador(1, 10, 1)
contador(10, 0, -1)

print('-' * 35 + f'\n{"PERSONALIZE SUA CONTAGEM":^35}\n' + '-' * 35)
contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
