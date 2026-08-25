class Termostato:

    def __init__(self) -> None:
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if temperatura % 0.5 != 0:
            raise ValueError(f"Temperatura de {temperatura} é inválida!")
        if temperatura < 16:
            self.__temperatura = 16
        elif temperatura > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = temperatura

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"
