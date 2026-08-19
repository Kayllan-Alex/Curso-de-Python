from rich import print

class funcionario:
    def __init__(self, nome="Vazio", setor="Vazio", cargo="Vazio"):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Olá eu sou [red]{self.nome}[/], trabalho no setor [blue]{self.setor}[/], e meu cargo é de [green]{self.cargo}[/]."


f1 = funcionario("Kayllan", "A+", "Gerente")
print(f1.apresentacao())