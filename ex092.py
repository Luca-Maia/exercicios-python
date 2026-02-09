pessoa = {}

nome = str(input('Nome: '))
pessoa['nome'] = nome

ano_de_nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = 2026 - ano_de_nascimento

ctps = int(input('Carteira de trabalho (0 não tem): '))
pessoa['ctps'] = ctps

if ctps != 0:
    ano_de_contratacao = int(input('Ano de Contratação: '))
    pessoa['contratacao'] = ano_de_contratacao

    salario = float(input('Salário: R$ '))
    pessoa['salario'] = salario

    tempo_de_trabalho = 2026 - ano_de_contratacao
    pessoa['aposentadoria'] = pessoa['idade'] + (20 - tempo_de_trabalho)

print('-=' * 30)

for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')