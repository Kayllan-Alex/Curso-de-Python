campeonato_brasileiro = (
    "Flamengo",
    "Palmeiras",
    "Santos",
    "Grêmio",
    "São Paulo",
    "Corinthians",
    "Atlético-MG",
    "Internacional",
    "Cruzeiro",
    "Vasco da Gama",
    "Botafogo",
    "Fluminense",
    "Bahia",
    "Athletico-PR",
    "Sport Recife",
    "Vitória",
    "Coritiba",
    "Goiás",
    "Avaí",
    "Ponte Preta",
)

for c in campeonato_brasileiro[0:5]:
    print(f"No top 5 está o(a) {c}")

for c in campeonato_brasileiro[20 : 15 - 1 : -1]:
    print(f"Do top 20 ao 15 está o(a) {c}")

for c in campeonato_brasileiro:
    print(
        c,
        end=" ",
    )
print(f"\nO fluminense está na posição {campeonato_brasileiro.index("Fluminense")}")
