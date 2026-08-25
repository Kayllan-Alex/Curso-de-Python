from pessoas import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo: str = "", setor: str = ""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        return f"O funcionario {self.nome} acabou de bater o ponto!"
