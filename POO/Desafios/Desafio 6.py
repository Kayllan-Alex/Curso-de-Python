from rich import print
from rich.panel import Panel
from rich.align import Align


class Gamer:
    jogos_favoritos = []

    def __init__(self, nome_da_pessoa="Vazio", nickname="Vazio"):
        self.nome = nome_da_pessoa
        self.nick = nickname

    def __str__(self):
        return f"O jogador [red]{self.nick}[/] foi cadastrado!"

    def adicionar_jogos(self, nome_do_jogo):
        Gamer.jogos_favoritos.append(nome_do_jogo)
        return f"O jogo [blue]{nome_do_jogo}[/] foi adicionado a sua lista de jogos favoritos!"

    def ficha(self):
        Gamer.jogos_favoritos.sort()
        conteudo = (
            f"[white]Nome do jogador: [blue]{self.nome}[/]\n"
            f"[white]Jogos favoritos: [/]"
        )
        for jogo in Gamer.jogos_favoritos:
            conteudo += f"\n:video_game: [purple]{jogo}[/]"
        painel = Panel(
            Align.center(conteudo),
            title=f"[blue]Jogador <[purple]{self.nick}[/]>",
            width=46,
        )
        return painel


user = Gamer("Kayllan Álex", "Kaywzz.py")
print(user.__str__())
print(user.adicionar_jogos("Hollow Knight"))
print(user.adicionar_jogos("Dead Cells"))
print(user.adicionar_jogos("Cod: Warzone"))
print(user.ficha())