from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str = "", idade: int = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self) -> str:
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso: str = "", turma: str = ""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        return f"O aluno {self.nome} acabou de fazer matrícula!"

    def estudar(self) -> str:
        return f"O aluno {self.nome} está estudando {self.curso} na turma {self.turma}"


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade: str = "", nivel: str = ""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        return f"O professor {self.nome} acabou de começar a dar aula!"

    def estudar(self) -> str:
        return f"O professor {self.nome} e da área {self.especialidade} tem um nível de {self.nivel}."


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo: str = "", setor: str = ""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        return f"O funcionario {self.nome} acabou de bater o ponto!"

    def estudar(self) -> str:
        return f"O funcionário {self.nome} tem um cargo de {self.cargo} e trabalha no setor {self.setor}."
