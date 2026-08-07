primeira_reta = float(input("Digite o comprimento da primeira reta: "))
segunda_reta = float(input("Digite o comprimento da segunda reta: "))
terceira_reta = float(input("Digite o comprimento da terceira reta: "))
if (
    primeira_reta + segunda_reta > terceira_reta
    and primeira_reta + terceira_reta > segunda_reta
    and segunda_reta + terceira_reta > primeira_reta
):
    print(f"O triângulo é possivel!")
    if primeira_reta == segunda_reta and segunda_reta == terceira_reta:
        print(f"Formara um triângulo equilátero.")
    elif (
        primeira_reta == segunda_reta
        or primeira_reta == terceira_reta
        or segunda_reta == terceira_reta
    ):
        print(f"Formara um triângulo isósceles.")
    else:
        print(f"Formara um triângulo escaleno.")
else:
    print(f"O triângulo é impossivel.")
