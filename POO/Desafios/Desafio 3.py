from rich import print
from rich.panel import Panel
from rich.align import Align


class Churrasco:
    consumo_por_pessoa = 0.4
    preco_por_kg = 82.40

    def __init__(self, titulo="Vazio", convidados=0):
        self.titulo = titulo
        self.convidados = convidados

    def quantia_suficiente(self):
        return self.convidados * Churrasco.consumo_por_pessoa

    def custo_total(self):
        return self.quantia_suficiente() * Churrasco.preco_por_kg

    def custo_individual(self):
        return self.custo_total() / self.convidados

    def analisar(self):
        conteudo = (
            f"Bem-vindo ao [red]{self.titulo}[/]! "
            f"O churrasco vai contar com [red]{self.convidados}[/] pessoas!\n"
            f"Cada pessoa comerá [red]{Churrasco.consumo_por_pessoa:.1f}[/] kg, "
            f"e o kg está custando R$ [red]{Churrasco.preco_por_kg:.2f}[/].\n"
            f"Então será preciso [red]{self.quantia_suficiente():.1f}[/] kg de churrasco.\n"
            f"O preço total sai por volta de R$ [red]{self.custo_total():.2f}[/].\n"
            f"E o custo individual fica aproximadamente R$ [red]{self.custo_individual():.2f}[/]."
        )
        painel = Panel(Align.center(conteudo), title="Churrasco", width=80)
        return painel


c1 = Churrasco("Kay do churras", 15)
print(c1.analisar())
