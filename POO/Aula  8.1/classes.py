from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(
        self,
        nome: str | None = None,
    ) -> None:
        super().__init__()
        self.nome: str | None = nome

    @abstractmethod
    def emitir_som(self) -> None:
        pass


class Pato(Animal):
    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de .. eh não sei o que um pato faz, quack talvez?")


class Cachorro(Animal):
    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de latir, Au Au Au para você também {self.nome}!")


class Spitz(Cachorro):
    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de latir, mas que coisa mais fofa!")


class Pitbull(Cachorro):
    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de latir, porém isso é bem medonho...")


class Gato(Animal):
    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de miar, talvez esteja com fome!")


class Galinha(Animal):
    def emitir_som(self) -> None:
        print(f"{self.nome} acabou de Po Po Por ovos!")
