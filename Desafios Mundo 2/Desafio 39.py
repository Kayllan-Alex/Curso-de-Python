ano_de_nascimento = int(input("Digite o ano em que você nasceu: "))
idade = 2026 - ano_de_nascimento
if idade < 18:
    print(f"Você tem apenas {idade} anos e não está apto para se alistar.")
    print(f"Volte daqui a {18 - idade} ano(s).")
elif idade == 18:
    print(f"Você tem {idade} anos e já está apto para o alistamento.")
else:
    print(f"Você excedeu o prazo de alistamento em {idade - 18} ano(s).")
    print("Compareça ao quartel imediatamente!")