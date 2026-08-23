from classes import *


def main():
    c1 = ContaBancaria("51254", "Kayllan Álex", 10000)
    c1.deposito(1000)
    "c1._titular = 'Karla'"  # Ele deixa, mas não é recomendado alterar um atributo protegido fora da classe
    "c1._ContaBancaria__saldo = 0"  # não é recomendado fazer isso fora da classe
    print(c1)


if __name__ == "__main__":
    main()
