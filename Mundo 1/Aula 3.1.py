primeiroNumero = int(input("Digite um número: "))
segundoNumero = int(input("Digite um segundo número: "))
soma = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero
exponenciacao = primeiroNumero ** segundoNumero
print(f"A soma vale {soma}", end=" ")
print(f"A subtração vale {subtracao}")
print(f"A multiplicação vale {multiplicacao}\n")
print(f"A divisão vale {divisao:.1f}")
print(f"A exponenciação vale {exponenciacao}")