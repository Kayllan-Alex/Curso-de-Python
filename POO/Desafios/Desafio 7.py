from rich import print
from rich.panel import Panel
from rich.align import Align


class Caneta:
    conteudo = ""

    def __init__(self, cor_da_caneta: str = "Nenhuma", caneta_tampada: bool = True):
        self.cor = cor_da_caneta.lower()
        self.tampada = caneta_tampada

    def destampar(self):
        self.tampada = False

    def escrever_na_tela(self, texto: str = ""):
        if self.tampada:
            return f":prohibited: [red]Impossivel escrever com uma caneta tampada![/]"
        else:
            match self.cor:
                case "vermelha":
                    return f"[red]{texto}[/]"
                case "azul":
                    return f"[blue]{texto}[/]"
                case "preta":
                    return f"[black]{texto}[/]"
                case _:
                    pass

    def quebrar_linha(self, quantas_vezes: int = 1):
        return "\n" * quantas_vezes

    def escrever_carta(self, texto: str = ""):
        if self.tampada:
            return f":prohibited: [red]Impossivel escrever com uma caneta tampada![/]"
        else:
            match self.cor:
                case "vermelha":
                    Caneta.conteudo += f"[red]{texto}[/]\n"
                case "azul":
                    Caneta.conteudo += f"[blue]{texto}[/]\n"
                case "preta":
                    Caneta.conteudo += f"[black]{texto}[/]\n"
                case _:
                    pass
        carta = Panel(Align.center(Caneta.conteudo), title="Carta", width=40)
        return carta


caneta1 = Caneta("Azul")
caneta2 = Caneta("Vermelha")
caneta3 = Caneta("Preta")
caneta1.destampar()
caneta2.destampar()
caneta3.destampar()
print(caneta1.escrever_na_tela("Olá eu sou o Caneta 1"))
print(caneta2.escrever_na_tela("Olá eu sou o Caneta 2"))
print(caneta3.escrever_na_tela("Olá eu sou o Caneta 3"))
print(caneta1.escrever_carta("Caneta 1"))
print(caneta2.escrever_carta("Caneta 2"))
print(caneta3.escrever_carta("Caneta 3"))
