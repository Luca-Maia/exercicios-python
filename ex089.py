alunos = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    alunos.append([nome, [nota1, nota2], media])

    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break

print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-' * 24)

for i, a in enumerate(alunos):
    print(f'{i:<4}{alunos[i][0]:<10}{alunos[i][2]:>8.1f}')
print('-' * 24)

while i != 999:
    i = int(input('Qual aluno você quer ver as notas? (999 para encerrar): '))
    if i != 999:
        print(f'Notas do aluno {i}: {alunos[i][1]}')
