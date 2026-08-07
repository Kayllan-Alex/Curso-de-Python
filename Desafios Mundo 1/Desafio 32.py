ano = int(input("Digite um ano de gosto seu: "))
if ano % 4 != 0:
    print(f"O ano {ano} não é bissexto!")
else:
    if ano % 100 == 0:
        print(f"O ano {ano} não é bissexto!")
    else:
        print(f"O ano {ano} é bissexto!")