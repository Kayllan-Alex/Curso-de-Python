from pessoas import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade: str = "", nivel: str = ""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        return f"O professor {self.nome} acabou de começar a dar aula!"
