frase = input("Digite uma frase para verificar se ela é um palindromo: ").replace(" ", "")
frase_inversa = ""
for i in range(len(frase) - 1, -1, -1):
    frase_inversa += frase[i]
if frase == frase_inversa:
    print(f"A frase é: {frase}")
    print(f"Ao contrario fica: {frase_inversa}")
    print("A frase é um palindromo!")
else:
    print(f"A frase é: {frase}")
    print(f"Ao contrario fica: {frase_inversa}")
    print("A frase não é um palindromo.")