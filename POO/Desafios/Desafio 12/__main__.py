from classes import *


def main():
    f1 = Mensalista("Kayllan", 2900)
    f1.calcular_salario()
    print(f1.analisar_salario())

    f2 = Horista("Kayllan", 15, 420)
    f2.calcular_salario()
    print(f2.analisar_salario())


if __name__ == "__main__":
    main()
