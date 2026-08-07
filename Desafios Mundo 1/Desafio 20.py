from random import shuffle
alunos = ["Clara", "David", "Sarah", "Keven"]
print("O professor irá sortear a ordem de apresentação do grupo composto por")
print("Clara, David, Sarah, Keven")
input("Pressione ENTER para fazer a ordem de apresentação.")
shuffle(alunos)
print(f"O primeiro vai ser o(a) {alunos[0]}")
print(f"O segundo vai ser o(a) {alunos[1]}")
print(f"O terceiro vai ser o(a) {alunos[2]}")
print(f"E por fim o último vai ser o(a) {alunos[3]}")