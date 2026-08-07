velocidade_do_carro = float(input("Digite a velocidade do carro: "))
print(
    f"Você está à {velocidade_do_carro}. Portanto será multado em R${(velocidade_do_carro - 80) * 7}!"
    if velocidade_do_carro > 80.0
    else f"Você está à {velocidade_do_carro}. Dirija com cuidado!"
)