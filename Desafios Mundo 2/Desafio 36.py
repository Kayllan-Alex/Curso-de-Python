valor_da_casa = float(input("Digite o valor da casa: "))
salario_do_comprador = float(input("Digite o seu salário: "))
daqui_quantos_anos_vai_pagar = float(input("Daqui quantos anos você irá pagar: "))
meses_de_prestacao = daqui_quantos_anos_vai_pagar * 12
valor_da_prestacao = valor_da_casa / meses_de_prestacao
if valor_da_prestacao <= (30 / 100 * salario_do_comprador):
    print(f"Você pode comprar a casa!")
else:
    print(f"Você não pode comprar a casa!")