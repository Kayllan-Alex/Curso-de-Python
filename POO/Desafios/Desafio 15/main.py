from classes import *
from rich import print, inspect


def main():
    d1 = Diario("123")
    d1.escrever = "Kayllan"

    print(d1.ler("123"))
    d1.escrever = "Aoba"

    print(d1.ler("123"))
    print(d1.ler("321"))


if __name__ == "__main__":
    main()
