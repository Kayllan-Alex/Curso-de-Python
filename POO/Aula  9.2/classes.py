class Numero:
    def __init__(self, valor: int) -> None:
        self.valor: int = valor

    def dobrar(self) -> None:
        self.valor *= 2

    def __str__(self) -> str:
        return f"O número é: {self.valor}"


class Texto:
    def __init__(self, texto: str | None = None) -> None:
        self.texto: str | None = texto

    def dobrar(self) -> None:
        if self.texto is not None:
            self.texto = self.texto + " " + self.texto

    def __str__(self) -> str:
        return f"O texto é: {self.texto}"


class Lista:
    def __init__(self, lista: list[str | float | int | bool] | None = None) -> None:
        self.lista: list[str | float | int | bool] | None = lista

    def dobrar(self) -> None:
        if self.lista is not None:
            self.lista = self.lista + self.lista

    def __str__(self) -> str:
        return f"O conteúdo da lista é: {self.lista}"


class Papel:
    def __init__(self) -> None:
        self.dobrado: bool | None = False

    def dobrar(self) -> None:
        if self.dobrado is not None:
            self.dobrado = True

    def __str__(self) -> str:
        return f"O papel está {'novo' if self.dobrado is False else 'dobrado'}"


class Casa:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"A casa não pode ser dobrada, mas ela é bonita!"


def tentar_dobrar(objeto: Numero | Texto | Lista | Papel) -> None:
    try:
        objeto.dobrar()
    except AttributeError:
        print(f"O objeto {objeto.__class__.__name__} não possui o método dobrar()")
