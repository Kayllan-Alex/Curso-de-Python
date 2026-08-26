class Carteira:
    def __init__(self, valor: float = 0) -> None:
        self.__saldo: float = valor

    def __str__(self) -> str:
        return f"Você tem R${self.__saldo:,.2f} guardado na carteira."

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, valor: float = 0) -> None:
        raise PermissionError("Você não tem autorização para essa ação!")

    def __eq__(self, outro: object = 0) -> bool:
        if isinstance(outro, Carteira):
            return self.__saldo == outro.__saldo
        return False

    def __le__(self, outro: object) -> bool:
        if isinstance(outro, Carteira):
            return self.__saldo <= outro.__saldo
        return False

    def __iadd__(self, valor: int | float = 0) -> Carteira:
        self.__saldo += valor
        return self

    def __isub__(self, valor: int | float = 0) -> Carteira:
        self.__saldo -= valor
        return self
