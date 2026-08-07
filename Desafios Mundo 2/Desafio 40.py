primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
media = (primeira_nota + segunda_nota) / 2
if media < 5:
    print(f"Com a média {media:.1f} você está REPROVADO!")
elif media < 7:
    print(f"Com a média {media:.1f} você está de recuperação!")
else:
    print(f"Com a média {media:.1f} você está APROVADO!!!!")