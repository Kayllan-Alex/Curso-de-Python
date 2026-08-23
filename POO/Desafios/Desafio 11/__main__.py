from classes import *


def main():
    t1 = Moto(60)
    print(t1.calcular_frete())

    t2 = Caminhao(120)
    print(t2.calcular_frete())

    t3 = Drone(8)
    print(t3.calcular_frete())


if __name__ == "__main__":
    main()
