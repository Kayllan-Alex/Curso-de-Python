alunos = []
while True:
    nome = input("Nome do aluno: ")
    notas = []
    for i in range(2):
        nota = float(input(f"{i + 1}ª nota: "))
        notas.append(nota)
    alunos.append([nome, notas])
    continuar = input("Deseja adicionar outro aluno? [S/N] ").lower()
    if continuar == "n":
        break
print("\nBOLETIM")
for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]

    media = (notas[0] + notas[1]) / 2

    print(f"{nome}: média {media:.1f}")
while True:
    print("\nAlunos:")
    for aluno in alunos:
        print(aluno[0])
    nome = input("Digite o nome do aluno para ver as notas (999 para sair): ")
    if nome == "999":
        break
    encontrado = False
    for aluno in alunos:
        if aluno[0].lower() == nome.lower():
            print(f"\nAluno: {aluno[0]}")
            print(f"Nota 1: {aluno[1][0]}")
            print(f"Nota 2: {aluno[1][1]}")
            encontrado = True
    if encontrado == False:
        print("Aluno não encontrado.")