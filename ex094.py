pessoas = list()

while True:
    dados = {}

    dados['nome'] = str(input('Nome: ')).strip()

    sexo = 'x'
    while sexo not in 'MF':
        sexo = str(input('Sexo? [M/F] ')).strip().upper()
        if sexo not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
    dados['sexo'] = sexo

    dados['idade'] = int(input('Idade: '))

    pessoas.append(dados.copy())

    r = 'x'
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
        if r not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')

    if r == 'N':
        break

print('=-' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoa(as) cadastradas.')

media_de_idade = sum(p['idade'] for p in pessoas) / len(pessoas)
print(f'B) A média de idade é de {media_de_idade:.2f} anos.')

print('C) As mulheres cadastradas foram', end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()

print('D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media_de_idade:
        print(f'\t-> Nome: {p['nome']}; Sexo: {p['sexo']}; Idade: {p['idade']}')
