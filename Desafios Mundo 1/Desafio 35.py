primeira_reta = float(input("Digite o comprimento da primeira reta: "))
segunda_reta = float(input("Digite o comprimento da segunda reta: "))
terceira_reta = float(input("Digite o comprimento da terceira reta: "))
if (
    primeira_reta + segunda_reta > terceira_reta
    and primeira_reta + terceira_reta > segunda_reta
    and segunda_reta + terceira_reta > primeira_reta
):
    print(
        f"Você pode formar um triângulo com as retas {primeira_reta} {segunda_reta} e {terceira_reta}"
    )
else:
    print(
        f"Você não pode formar um triângulo com as retas {primeira_reta} {segunda_reta} e {terceira_reta}"
    )
