alunos = dict()
nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))
if media >= 6:
    situacao = "aprovado"
else:
    situacao = "reprovado"
alunos["nome"] = nome
alunos["media"] = media
alunos["situação"] = situacao
print(f"O aluno {alunos['nome']} está {alunos['situação']}")