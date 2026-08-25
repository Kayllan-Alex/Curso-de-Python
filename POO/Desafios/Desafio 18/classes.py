class Retangulo:
    def __init__(self, base: float = 0.0, altura: float = 0.0) -> None:
        self._base: float = base
        self._altura: float = altura
        self._area: float = altura * base

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, valor: float = 0.0) -> None:
        self._base: float = valor

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, valor: float = 0.0) -> None:
        self._altura: float = valor

    @property
    def area(self) -> float:
        return self._area

    @area.setter
    def area(self) -> None:
        self._area: float = self.altura * self.base

    def medidas(self) -> str:
        return (
            f"Base = {self._base:.1f}\n"
            f"Altura = {self._altura:.1f}\n"
            f"Área = {self._area:.1f}"
        )
