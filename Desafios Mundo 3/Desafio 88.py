from random import sample
jogos = []
quantidade = int(input("Quantos jogos você quer gerar? "))
for _ in range(quantidade):
    jogo = sample(range(1, 61), 6)
    jogos.append(jogo)
for i, jogo in enumerate(jogos, 1):
    print(f"Jogo {i}: {jogo}")