from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
from rich.align import Align


class Transporte(ABC):
    def __init__(self, distancia: float = 0.0) -> None:
        super().__init__()
        self.distancia = distancia

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    def __init__(self, distancia: float = 0) -> None:
        super().__init__(distancia)
        self.frete: float = 1.50

    def calcular_frete(self):
        conteudo = (f"O frete da Moto custa [green]R${self.frete:,.2f}[/]\n"
                    f"Pois ela vai rapidamente pelas estradas e carrega pouco peso\n"
                    f"Para um distância de [red]{self.distancia}Km[/]\n"
                    f"O frete sai por volta de [green]R${self.frete * self.distancia:,.2f}[/]")
        painel = Panel(Align.center(conteudo),
                       title="Frete by < Moto >", width=100)
        return painel


class Caminhao(Transporte):
    def __init__(self, distancia: float = 0) -> None:
        super().__init__(distancia)
        self.frete: float = 5.50

    def calcular_frete(self):
        if self.distancia < 50:
            return Panel(Align.center("Distância minima de 50Km"), title="[red]Error[/] by < Caminhão >", width=100, style="red")
        else:
            conteudo = (f"O frete do Caminhão custa [green]R${self.frete:,.2f}[/]\n"
                        f"Pois o caminhão vai mais lentamente e carrega mais peso\n"
                        f"Para uma distância de [red]{self.distancia}Km[/]\n"
                        f"O frete sai por volta de [green]R${self.distancia * self.frete:,.2f}[/]")
            painel = Panel(Align.center(conteudo),
                           title="Frete by < Caminhão >", width=100)
            return painel


class Drone(Transporte):
    def __init__(self, distancia: float = 0) -> None:
        super().__init__(distancia)
        self.frete: float = 9.50

    def calcular_frete(self):
        if self.distancia > 10:
            return Panel(Align.center("Distância máxima de 10Km"), title="[red]Error[/] by < Drone >", width=100, style="red")
        else:
            conteudo = (f"O frete do drone custa [green]R${self.frete:,.2f}[/]\n"
                        f"Pois o drone voa rapidamente e carrega pouquissima carga\n"
                        f"Para uma distância de [red]{self.distancia}Km[/]\n"
                        f"O frete sai por volta de [green]{self.distancia * self.frete:,.2f}[/]")
            painel = Panel(Align.center(conteudo),
                           title="Frete by < Drone >", width=100)
            return painel
