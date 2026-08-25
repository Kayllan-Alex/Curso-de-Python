from classes import *
from rich import print, inspect


def main():
    c = Credencial()
    c.senha = "123"
    print(c.senha)
    print(c.validar("123"))


if __name__ == "__main__":
    main()
