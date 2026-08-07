frase = input("Digite uma frase: ").lower()
print(f"A frase contém {frase.count('a')} letras A")
print(f"Ela aparece pela primeira vez na {frase.find('a')}ª posição")
print(f"E por fim aparece pela ultima vez na {frase.rfind('a')}ª posição")