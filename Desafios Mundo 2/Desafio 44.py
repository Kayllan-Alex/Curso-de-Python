print("O valor desse produto é de R$2500.00")
print("""Qual a forma de pagamento?
      [1] À vista em dinheiro/cheque com 10% de desconto.
      [2] À vista no cartão com 5% de desconto.
      [3] Em até 2x no cartão.
      [4] Em até 3x no cartão com 20% de juros.""")
escolha = int(input())
if escolha == 1:
    print(f"A vista com 10% de desconto fica no valor de R${2500 - (10/100 * 2500)}")
elif escolha == 2:
    print(f"A vista com 5% de desconto fica no valor de R${2500 - (5/100 * 2500)}")
elif escolha == 3:
    print(
        f"Parcelado em 2 vezes fica no valor de R${2500 / 2} no primeiro mês e R${2500 / 2} no segundo mês"
    )
elif escolha == 4:
    valor_total = (2500 + (20 / 100) * 2500) / 3
    print(
        f"""Parcelado em 3 vezes fica no valor de R${valor_total} no primeiro mês, no segundo fica R${valor_total}, e por fim no terceiro mês fica R${valor_total}"""
    )
else:
    print("Digite um opção válida!")