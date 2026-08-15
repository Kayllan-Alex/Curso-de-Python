from random import randint
jogadores = {
    'jogador1': randint(0, 6),
    'jogador2': randint(0, 6),
    'jogador3': randint(0, 6),
    'jogador4': randint(0, 6),
}
print("Valores sorteados:")
for j, v in jogadores.items():
    print(f"O jogador {j} tirou {v}")
ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
print("\nRanking:")
for pos, (j, v) in enumerate(ranking, 1):
    print(f"{pos}º lugar: {j} com {v}")