class Mae:
    def __init__(self, nome: str | None = None) -> None:
        self.nome: str | None = nome

    def fazer_pudim(self) -> None:
        print(f"{self.nome} fez PUDIM com leite condensado e calda.")

    def fritar_coxinha(self) -> None:
        print(f"{self.nome} fritou COXINHA com óleo de soja.")


class Filho(Mae):
    def fritar_coxinha(self) -> None:
        print(f"{self.nome} fritou COXINHA na Air Fryer.")


class Filha(Mae):
    def fazer_pudim(self) -> None:
        print(f"{self.nome} fez PUDIM com leite ninho com nuttela.")
