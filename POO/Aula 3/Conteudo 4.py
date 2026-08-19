from rich import print
from rich import inspect


class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id="0", nome="Vazio", saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print("Conta criada!")

    def __str__(self):
        return (
            f"A conta de ID: {self.id}, cujo nome do titular é "
            f"{self.titular}, tem saldo de R${self.saldo:.2f}"
        )

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} foi autorizado " f"na conta de ID: {self.id}")
        print(f"Sua conta tem atualmente R${self.saldo:.2f}")

    def saque(self, valor):
        if valor > self.saldo:
            print(f"Saque de {valor} não autorizado. Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(
                f"Saque de R${valor:.2f} foi autorizado " f"na conta de ID: {self.id}"
            )
            print(f"Sua conta tem atualmente R${self.saldo:.2f}")


conta1 = ContaBancaria("152653", "Kayllan", 5000)
inspect(conta1)
