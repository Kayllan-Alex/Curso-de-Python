from classes import *


def main():
    p1 = Mago("Kayllan", 1500)
    p2 = Guerreiro("Yuri", 1200)
    print(p1.stats())
    print(p2.stats())
    print(p2.atacar(p1, 100))
    p1.receber_dano(100)
    print(p1.atacar(p2, 80))
    p2.receber_dano(80)
    print(p1.curar())
    print(p2.curar())
    print(p1.stats())
    print(p2.stats())


if __name__ == "__main__":
    main()
