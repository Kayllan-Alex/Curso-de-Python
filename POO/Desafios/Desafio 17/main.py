from classes import *
from rich import print


def main():
    c1 = ContaBancaria("Kayllan Álex", 2621, "12345678")
    print(c1.verificar_conta())
    print(c1.sacar_dinheiro(0))
    print(c1.depositar(0))
    print(c1.verificar_conta())


if __name__ == "__main__":
    main()
