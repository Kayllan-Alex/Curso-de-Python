def header():
    """
    -> Imprime um cabeçalho na tela.
    :return: Sem retorno
    """
    print('-' * 30 + f'\n{"FATORIAL":^30}\n' + '-' * 30)


def fatorial(num, show=False):
    """
    -> Realiza calculo de fatórial de um número inteiro.
    :param num: Parâmetro que recebe o valor a ser calculado o fatórial
    :param show: Parâmetro Opcional, que mostra ou não o calculo do fatórial
    :return: Retorna o valor fatórial de um número inteiro N.
    """
    fato = 1
    for cont in range(num, 0, -1):
        fato *= cont
        if show:
            print(f'{cont}', end=' x ' if cont != 1 else ' = ')
    return fato


print(fatorial(10, True)) 
print()
print(fatorial(7)) 
print()
help(fatorial)  
