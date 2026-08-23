from abc import ABC, abstractmethod
from math import pi


class Poligono(ABC):
    def __init__(self, lados: int = 0) -> None:
        self.lados = lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Quadrado(Poligono):
    def __init__(self, lado: int = 1) -> None:
        super().__init__(4)
        self.lado = lado

    def perimetro(self) -> float:
        return self.lado * 4

    def area(self) -> float:
        return self.lado**2


class Circulo(Poligono):
    def __init__(self, raio: int = 1) -> None:
        super().__init__(0)
        self.raio = raio

    def perimetro(self) -> float:
        return 2 * pi * self.raio

    def area(self) -> float:
        return 2 * pi**self.raio
