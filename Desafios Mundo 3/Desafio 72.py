numeros_por_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
while True:
    numero_selecionado = int(input("Digite um número de 0 a 20: "))
    if numero_selecionado not in range(0, 20 + 1):
        print("Tente novamente!")
    else:
        break
print(
    f"O número {numero_selecionado} escrito por extenso é {numeros_por_extenso[numero_selecionado]}"
)