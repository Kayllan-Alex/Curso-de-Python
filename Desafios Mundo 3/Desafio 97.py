# Função para imprimir mensagens dentro de cabeçalho com bordas
def escreva(mensagem):
    print('-' * (len(mensagem) + 4))
    print(f'  {mensagem}  ')
    print('-' * (len(mensagem) + 4))

escreva('Olá, mundo')
escreva('Python é a melhor linguagem do mundo')
escreva('Python é maior que Java')