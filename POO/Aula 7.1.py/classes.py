class Avaliacao:
    def __init__(self, nome: str = "", disciplina: str = "", nota: float = 0.0) -> None:
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota  # Atributo protegido (#)

    def get_nota(self):  # Método getter
        return self._nota

    def set_nota(self, valor):  # Método setter
        if 0 < valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida!")