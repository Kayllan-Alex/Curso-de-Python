while True:
    tabuada_desejada = int(input("Digite qual a tabuada você deseja ver: "))
    if tabuada_desejada < 0:
        break
    else:
        for c in range(0, 10 + 1):
            print(f"{tabuada_desejada} x {c} = {tabuada_desejada * c}")
print(f"Programa de tabuada encerrado.")
