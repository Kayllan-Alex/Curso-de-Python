from abc import ABC, abstractmethod
from random import randint
from rich import print


class Personagem(ABC):
    def __init__(self, nome: str = "", vida: float = 0.0) -> None:
        super().__init__()
        self.nome = nome
        self.vida = vida

    @abstractmethod
    def stats(self) -> str:
        pass

    @abstractmethod
    def receber_dano(self, dano) -> None:
        pass

    @abstractmethod
    def atacar(self, alvo, dano) -> str:
        pass

    @abstractmethod
    def curar(self) -> str:
        pass


class Mago(Personagem):
    def __init__(self, nome: str = "", vida: float = 0) -> None:
        super().__init__(nome, vida)
        self.magia = randint(100, 200)

    def curar(self) -> str:
        self.vida += self.magia
        return f"O mago {self.nome} recuperou {self.magia} de vida com sua magia das estrelas."

    def atacar(self, alvo, dano) -> str:
        alvo.receber_dano(dano)
        return (
            f"O mago [blue]{self.nome}[/] atacou [red]{alvo.nome}[/] com sua magia de [yellow]fogo[/]\n"
            f"deixando o oponente com [red]-{dano} de vida.[/]"
        )

    def stats(self) -> str:
        return (
            f"[bold purple]{self.nome}[/] é da classe [blue]{type(self).__name__}[/]\n"
            f"O atributo de sua classe da a ele chance de recuperar mais vida\n"
            f"está com [red]{self.vida}HP[/]"
        )

    def receber_dano(self, dano) -> None:
        self.vida -= dano * 2


class Guerreiro(Personagem):
    def __init__(self, nome: str = "", vida: float = 0) -> None:
        super().__init__(nome, vida)
        self.atadura = randint(35, 60)

    def curar(self) -> str:
        self.vida += self.atadura
        return f"O guerreiro {self.nome} recuperou {self.atadura} de vida com a sua atadura."

    def atacar(self, alvo, dano) -> str:
        dano *= 2
        alvo.receber_dano(dano)
        return (
            f"O guerreiro [red]{self.nome}[/] atacou [blue]{alvo.nome}[/] com suas láminas do [red]chaos[/]\n"
            f"causando o dobro do [red]dano[/], deixando o oponente com [red]-{dano} de vida.[/]"
        )

    def stats(self) -> str:
        return (
            f"[bold purple]{self.nome}[/] é da classe [red]{type(self).__name__}[/]\n"
            f"O atributo de sua classe da a ele o dobro de dano\n"
            f"está com [red]{self.vida}HP[/]"
        )

    def receber_dano(self, dano) -> None:
        self.vida -= dano
