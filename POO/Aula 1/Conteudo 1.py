# Declaração da classe
class Gafanhoto:
    # Método construtor
    def __init__(self):
        self.nome = ""
        self.idade = 0

    # Método de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"


# Declaração dos objetos
g1 = Gafanhoto()
g1.nome = "Kayllan"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Keila"
g2.idade = 20
g2.aniversario()
print(g2.mensagem())
