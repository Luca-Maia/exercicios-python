def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de alunos.
    
    :param notas: uma ou mais notas dos alunos.
    :param sit: valor opcional, para mostrar a situação do aluno (RUIM, BOA, ÓTIMA)
    :return: dicionário com várias informações sobre a turma ou aluno
    """
    resp = dict()

    resp['total'] = len(notas)
    resp['maior'] = max(notas)
    resp['menor'] = min(notas)
    resp['media'] = sum(notas) / len(notas)

    if sit:
        if resp['media'] < 7.00:
            resp['situação'] = 'RUIM'
        elif  7.00 < resp['media'] < 9.00:
            resp['situação'] = 'BOA'
        else:
            resp['situação'] = 'ÓTIMA'

    return resp

resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)
