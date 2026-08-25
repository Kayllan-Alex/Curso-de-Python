from classes import *
from rich import print, inspect


def main():
    r = Retangulo(2, 4)
    print(r.medidas())
    r.base = 4
    r.altura = 8
    r.area
    print(r.medidas())
    inspect(r, private=True, methods=True)


if __name__ == "__main__":
    main()
