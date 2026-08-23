class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id="0", nome="Vazio", saldo=0):
        self.id = id  # atributo público
        self._titular = nome  # atributo protegido
        self.__saldo = saldo  # atributo privado
        print("Conta criada!")

    def __str__(self):
        return (
            # f"A conta de ID: {self.id}, cujo nome do titular é "
            # f"{self._titular}, tem saldo de R${self.__saldo:,.2f}\n"
            f"{self.__dict__}"
        )

    def deposito(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(
            f"Depósito de R${valor:,.2f} foi autorizado " f"na conta de ID: {self.id}"
        )
        print(f"Sua conta tem atualmente R${self.__saldo:,.2f}")

    def saque(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque de {valor} não autorizado. Saldo insuficiente!")
        else:
            self.__saldo -= valor
            print(
                f"Saque de R${valor:,.2f} foi autorizado " f"na conta de ID: {self.id}"
            )
            print(f"Sua conta tem atualmente R${self.__saldo:,.2f}")
