from classes import *
from rich import print, inspect


def main():
    t = Termostato()
    try:
        t.temperatura = 25.2
    except Exception as e:
        print(f"Houve um problema: {e}")
    print(t.ftemperatura)
    # inspect(t, private=True, methods=True)


if __name__ == "__main__":
    main()
