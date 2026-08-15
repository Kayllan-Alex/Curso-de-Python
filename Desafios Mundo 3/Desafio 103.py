def ficha(nome_jogador='<desconhecido>', qtd_gols=0):
    print(f'O jogador {nome_jogador} fez {qtd_gols} gol(s) no campeonato.')


nome = input('Nome do jogador: ').strip().capitalize()
gols = input('Quantidade de gols: ').strip()
gols = int(gols) if gols.isnumeric() else 0

ficha(qtd_gols=gols) if nome == '' else ficha(nome, gols)