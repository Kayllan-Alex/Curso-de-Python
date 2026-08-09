palavras = (
    "aprender",
    "programar",
    "linguagem",
    "python",
    "curso",
    "gratis",
    "estudar",
    "praticar",
    "trabalhar",
    "mercado",
    "programador",
    "futuro",
)

for palavra in palavras:
    print(f"{palavra}:", end=" ")

    for letra in palavra:
        if letra in "aeiou":
            print(letra, end=" ")

    print()
