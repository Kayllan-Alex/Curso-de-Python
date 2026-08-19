from rich import print
from time import sleep


class Livro:
    pagina_atual = 1

    def __init__(self, titulo="Vazio", paginas=0):
        self.titulo = titulo
        self.paginas = paginas

    def __str__(self):
        return (
            f":open_book: Você acabou de enviar o livro: "
            f"[red]{self.titulo}[/], que contém [blue]{self.paginas}[/] "
            f"páginas :page_facing_up:."
        )

    def abrir_livro(self):
        return (
            f"Você abriu o livro {self.titulo}, que contém "
            f"{self.paginas} páginas.\n"
            f"Você está na página {Livro.pagina_atual}"
        )

    def avancar_pagina(self, paginas):
        for c in range(paginas):
            if Livro.pagina_atual < self.paginas:
                Livro.pagina_atual += 1
                print(f"Pág [red]{Livro.pagina_atual}[/]", end=" ")
                sleep(0.25)
            else:
                break

        if Livro.pagina_atual >= self.paginas:
            return (
                f"\nAgora você está na página [red]{Livro.pagina_atual}[/].\n"
                f"[red]Você atingiu o limite máximo de páginas![/]"
            )

        else:
            return (
                f"\nVocê avançou [blue]{paginas}[/] páginas, "
                f"agora você está na página [red]{Livro.pagina_atual}[/]."
            )


l1 = Livro("A Espera de um Milagre", 10)
print(l1.abrir_livro())
print(l1.avancar_pagina(10))
print(l1.avancar_pagina(10))
print(l1.avancar_pagina(98))
