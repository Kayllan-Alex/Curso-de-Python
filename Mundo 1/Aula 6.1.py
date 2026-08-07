primera_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
terceira_nota = float(input("Digite sua terceira nota: "))
quarta_nota = float(input("Digite sua quarta nota: "))
media = (primera_nota + segunda_nota + terceira_nota + quarta_nota) / 4
print(f"A sua média foi {media:.1f}")

# print(f"Parábens pelo esforço!" if media >=6 else "Estude mais!") Simplificado!

if media >= 6:
    print("Sua média foi boa parábens!")
else:
    print("Sua nota foi ruim estude mais!")
