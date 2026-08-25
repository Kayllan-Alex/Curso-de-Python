class Diario:
    def __init__(self, senha: str = "12345678") -> None:
        self.__senha = senha
        self.__conteudo = ""

    @property
    def escrever(self) -> str:
        return self.__conteudo

    @escrever.setter
    def escrever(self, texto: str) -> None:
        self.__conteudo += texto + "\n"

    def ler(self, senha: str = "") -> str | None:
        if senha == self.__senha:
            return self.__conteudo
        return f"Senha inválida!"
