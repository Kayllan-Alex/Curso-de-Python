salario = float(input("Digite seu salário: "))
if salario > 1250:
    print(f"Você recebeu um aumento de 10% ficando com o salário de R${salario + (10/100) * salario:.2f}")
else:
    print(f"Você recebeu um aumento de 15% ficando com o salário de R${salario + (15/100) * salario:.2f}")