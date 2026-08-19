from pessoas import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso: str = "", turma: str = ""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        return f"O aluno {self.nome} acabou de fazer matrícula!"
