from classes import *
from rich import print, inspect


def main():
    a1 = Aluno("Kayllan Álex", 2008, "ADS")
    a1.add_curso("enf")
    a1.curso = "enf"
    a1.nascimento = 2010
    inspect(a1, private=True, methods=True)


if __name__ == "__main__":
    main()
