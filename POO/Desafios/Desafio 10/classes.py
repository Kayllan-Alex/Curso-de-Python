from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta ---\n")

    def ferver_agua(self):
        print("1. Fervendo a água a 100°.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print("3. Servindo em xícara pequena.")


class Cha(BebidaQuente):
    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.")


class Leite(BebidaQuente):
    def misturar(self):
        print("2. Passando favor pressurizada pelo bico do leite.")

    def servir(self):
        print("3. Servindo na caneca grande.")
