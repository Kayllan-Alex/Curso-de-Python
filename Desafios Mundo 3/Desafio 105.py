def notas_aluno(*args, situacao=False):
    """
    -> Função para análisar notas e situação dos alunos de uma turma
    :param args: Parâmetro recebe uma ou várias notas informadas dos alunos de uma turma.
    :param situacao: Parâmetro opcional, indica se quer ou não informar a situação da turma no dicionário.
    :return: Retorna um dicionário com as informações de toda a turma.
    """
    info_alunos = dict(total=len(args), maior=max(args), menor=min(args), media=sum(args) / len(args))
    if situacao:
        if info_alunos['media'] < 5:
            info_alunos['situacao'] = 'RUIM'
        elif info_alunos['media'] < 7:
            info_alunos['situacao'] = 'RAZOÁVEL'
        elif info_alunos['media'] < 10:
            info_alunos['situacao'] = 'ÓTIMO'
    return info_alunos


resp = notas_aluno(5.5, 9.5, 10, 6.5, situacao=True)
print(f'Dicionário de dados: {resp}')
print()
help(notas_aluno)
