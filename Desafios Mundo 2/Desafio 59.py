primeiro_numero = int(input("Digite o primeiro valor: "))
segundo_numero = int(input("Digite o segundo valor: "))
opcao_escolhida = None
while opcao_escolhida != 5:
    print("Escolha uma dessas opções:")
    print("[1] Somar os números")
    print("[2] Multiplicar os números")
    print("[3] Ver qual é maior")
    print("[4] Mudar um dos números")
    print("[5] Encerrar o programa")
    opcao_escolhida = int(input("Digite aqui: "))
    match opcao_escolhida:
        case 1:
            print(
                f"A soma de {primeiro_numero} + {segundo_numero} é igual à {primeiro_numero + segundo_numero}"
            )
        case 2:
            print(
                f"A multiplicação de {primeiro_numero} x {segundo_numero} é igual à {primeiro_numero * segundo_numero}"
            )
        case 3:
            if primeiro_numero > segundo_numero:
                print(f"O {primeiro_numero} é maior que {segundo_numero}")
            elif segundo_numero > primeiro_numero:
                print(f"O {segundo_numero} é maior que {primeiro_numero}")
            else:
                print("Ambos os números são iguais")
        case 4:
            primeiro_numero = int(
                input("Digite um novo valor para o primeiro número: ")
            )
            segundo_numero = int(input("Digite um novo valor para o segundo número: "))
        case _:
            print("Opção inválida!")
print("Fim do programa.")
