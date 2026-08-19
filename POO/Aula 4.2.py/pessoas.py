class Pessoa:
    def __init__(self, nome: str = "", idade: int = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
