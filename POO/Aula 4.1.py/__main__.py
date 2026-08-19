from rich import print, inspect
from classes import Aluno, Professor, Funcionario

a1 = Aluno("Kayllan", 17, "Redes de Computadores", "2B")
a1.fazer_aniversario()
print(a1.fazer_matricula())
# inspect(a1)

p1 = Professor("Pedro", 25, "Física", "Doutor")
p1.fazer_aniversario()
print(p1.dar_aula())
# inspect(p1)

f1 = Funcionario("Diego", 17, "Zelador", "a-B1")
f1.fazer_aniversario()
print(f1.bater_ponto())
# inspect(f1)
