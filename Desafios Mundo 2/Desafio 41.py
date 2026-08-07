ano_de_nascimento = int(input("Digite o ano de seu nascimento: "))
idade = 2026 - ano_de_nascimento
if idade <= 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infantil"
elif idade <= 19:
    categoria = "Júnior"
elif idade <= 20:
    categoria = "Sênior"
else:
    categoria = "Master"
print(f"Você tem {idade} anos e está na categoria {categoria}.")