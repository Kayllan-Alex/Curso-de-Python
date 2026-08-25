class Avaliacao:

    def __init__(self, nome: str = "", disciplina: str = "", nota: float = 0.0) -> None:
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    @property
    def nota(self) -> float:
        return self._nota

    @nota.setter
    def nota(self, valor: float) -> None:
        if 0 < valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida!")

    @nota.deleter
    def nota(self):
        pass
