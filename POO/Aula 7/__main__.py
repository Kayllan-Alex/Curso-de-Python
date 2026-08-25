from classes import *
from rich import print, inspect


def main():
    av1 = Avaliacao("Kayllan", "Física")
    av1.nota = -3.5
    print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}")
    inspect(av1, private=True)


if __name__ == "__main__":
    main()
