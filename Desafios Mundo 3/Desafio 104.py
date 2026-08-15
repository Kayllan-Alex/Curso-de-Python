def leiaint(msg):
    valor = input(msg).strip()
    while not valor.isnumeric():
        print('\n\33[31mERRO! Informe um valor inteiro corretamente...\33[m')
        valor = input(msg).strip()
    return valor

n = leiaint('Digite um número: ')
print(f'Você digitou o número: {n}')
