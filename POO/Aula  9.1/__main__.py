from classes import *


def main():
    c1 = Carteira(100)
    c2 = Carteira(200)
    print(c1 == c2)
    c1 += 50
    c2 -= 100
    print(c1)
    print(c2)
    if c1 == c2:
        print("Vocês tem o mesmo valor.")
    else:
        print("Vocês tem valores diferentes.")
    if c1 <= c2:
        print("A segunda carteira tem mais dinheiro.")
    else:
        print("A primeira carteira tem mais dinheiro.")


if __name__ == "__main__":
    main()
