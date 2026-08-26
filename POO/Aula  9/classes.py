from functools import singledispatchmethod


class Analisador:

    @singledispatchmethod
    def analisar(self, valor: None = None) -> None:
        print(f"Não foi possível analisar o valor: {valor}.")

    @analisar.register
    def _(self, valor: int) -> None:
        print(f"{valor} é um número inteiro.")

    @analisar.register
    def _(self, valor: float) -> None:
        print(f"{valor} é um número real.")

    @analisar.register
    def _(self, texto: str) -> None:
        print(f"{texto} é um texto.")

    @analisar.register(list)
    def _(self, lista: list[int | str | float | bool]) -> None:
        print(f"{lista} é uma lista.")

    @analisar.register(tuple)
    def _(self, tupla: tuple[int | str | float | bool, ...]) -> None:
        print(f"{tupla} é uma tupla.")

    @analisar.register(dict)
    def _(
        self, dicionario: dict[int | str | float | bool, int | str | float | bool]
    ) -> None:
        print(f"{dicionario} é um dicionario")
