from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from rich.align import Align


class Funcionario(ABC):
    def __init__(
        self,
        nome: str = "",
    ):
        self.nome = nome
        self.salario_minimo: float = 1621
        self.inss: float = 7.5

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        conteudo = (
            f"[red]{self.nome}[/] é um [purple]{type(self).__name__}[/]\n"
            f"E ganha [green]R${self.salario:,.2f}[/]\n"
            f"Que é equivalente a [yellow]{self.salario / self.salario_minimo:,.2f}[/] salários mínimos."
        )
        painel = Panel(Align.center(conteudo), title=f"Action by < {self.nome} >")
        return painel


class Horista(Funcionario):
    def __init__(
        self,
        nome: str = "",
        valor_por_hora: float = 0.0,
        horas_trabalhadas: float = 0.0,
    ):
        super().__init__(nome)
        self.valor_por_hora = valor_por_hora
        self.horas_trabalhadas = horas_trabalhadas
        self.salario = 0

    def calcular_salario(self):
        self.salario = self.valor_por_hora * self.horas_trabalhadas
        self.salario = self.salario - ((self.inss / 100) * self.salario)


class Mensalista(Funcionario):
    def __init__(self, nome: str = "", salario_bruto: float = 0):
        super().__init__(nome)
        self.salario = 0
        self.salario_bruto = salario_bruto

    def calcular_salario(self):
        self.salario = self.salario_bruto - ((self.inss / 100) * self.salario_bruto)
