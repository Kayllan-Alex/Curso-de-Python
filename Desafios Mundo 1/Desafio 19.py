from random import choice
alunos = ["Karla", "Kayllan", "Breno", "Yuri"]
print("O professor vai escolher 1 aluno(a) para apagar o quadro.")
print("Participantes: Karla, Kayllan, Breno e Yuri.")
input("Pressione ENTER para o professor escolher...")
escolhido = choice(alunos)
print(f"O aluno(a) escolhido foi {escolhido}.")