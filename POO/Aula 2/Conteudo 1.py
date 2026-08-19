class Gafanhoto:
    """
    Classe Gafanhoto representa um gafanhoto com atributos de nome, idade e sexo.
    Possui métodos para incrementar a idade e gerar uma mensagem descritiva sobre o gafanhoto.
    """

    def __init__(self, nome="", idade=0, sexo=""):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        if self.sexo.upper() == "F":
            return f"{self.nome} é uma gafanhota e tem {self.idade} anos de idade"
        else:
            return f"{self.nome} é um gafanhoto e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade} ; sexo = {self.sexo}"


g1 = Gafanhoto("Kayllan", 17, "M")
g1.aniversario()

print(g1.__class__)  # Attribute
print(g1.__getstate__())  # Method
print(g1.__dict__)  # Attribute
# print(g1.__doc__) Dunder Attribute
