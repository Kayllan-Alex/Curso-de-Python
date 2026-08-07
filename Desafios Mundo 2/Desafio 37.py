numero = int(input("Digite um número: "))
print("""Escolha uma opção:
[1] Conversão binária
[2] Conversão octal
[3] Conversão hexadecimal""")
escolha_do_usuario = int(input("Sua escolha: "))
if escolha_do_usuario == 1:
    print(f"O número {numero} em binário é {bin(numero)}")
elif escolha_do_usuario == 2:
    print(f"O número {numero} em octal é {oct(numero)}")
elif escolha_do_usuario == 3:
    print(f"O número {numero} em hexadecimal é {hex(numero)}")
else:
    print("Faça uma escolha válida!")