from rich import print, inspect


class Pessoa:
    def __init__(self, nome: str = "", idade: int = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso: str = "", turma: str = ""):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        return f"O aluno {self.nome} acabou de fazer matrícula!"


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade: str = "", nivel: str = ""):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        return f"O professor {self.nome} acabou de começar a dar aula!"


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo: str = "", setor: str = ""):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        return f"O funcionario {self.nome} acabou de bater o ponto!"


a1 = Aluno("Kayllan", 17, "Redes de Computadores", "2B")
a1.fazer_aniversario()
print(a1.fazer_matricula())
# inspect(a1)

p1 = Professor("Pedro", 25, "Física", "Doutor")
p1.fazer_aniversario()
print(p1.dar_aula())
# inspect(p1)

f1 = Funcionario("Diego", 17, "Zelador", "a-B1")
f1.fazer_aniversario()
print(f1.bater_ponto())
# inspect(f1)
