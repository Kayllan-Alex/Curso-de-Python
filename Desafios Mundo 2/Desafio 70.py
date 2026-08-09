total_gasto = produtos_caros = produto_mais_barato = nome_do_produto_mais_barato = 0
while True:
    nome_do_produto = input("Digite o nome do produto: ")
    preco_do_produto = float(input("Digite o preço do produto: "))
    total_gasto += preco_do_produto
    if produto_mais_barato == 0:
        nome_do_produto_mais_barato = nome_do_produto
        produto_mais_barato += preco_do_produto
    if preco_do_produto < produto_mais_barato:
        produto_mais_barato = preco_do_produto
        nome_do_produto_mais_barato = nome_do_produto
    if preco_do_produto > 1000:
        produtos_caros += 1
    while True:
        continuar = input("Deseja continuar [S] ou [N]: ").upper()
        if continuar in ["S", "N"]:
            break
        print("Digite apenas [S] ou [N]: ")
    if continuar == "N":
        break
print(f"O total gasto foi de R${total_gasto:.2f}")
print(f"{produtos_caros} produtos custam mais de R$1000.00")
print(
    f"E o nome do produto mais barato é {nome_do_produto_mais_barato} custando apenas R${produto_mais_barato:.2f}"
)