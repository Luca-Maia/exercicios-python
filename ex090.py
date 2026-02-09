aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))

if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print(f'Situação é igual a {aluno["situacao"]}')
