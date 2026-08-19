from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")
tabela.add_column("Nome", justify="left", style="red")
tabela.add_column("Preço", justify="center", style="blue")
tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Caderno", "R$19,99")
tabela.add_row("Corretivo", "R$2,00")
print(tabela)
