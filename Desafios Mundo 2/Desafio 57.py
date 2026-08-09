sexo = None
while sexo not in ["M", "F"]:
    sexo = input("Digite o seu sexo [F] ou [M]: ").upper()
if sexo == "F":
    print("Você é do sexo feminino!")
else:
    print("Você é do sexo masculino!")
