pessoas = list()
dados = list()

while True:
    dados.append(str(input('Name: ')))
    dados.append(float(input('Weight: ')))
    pessoas.append(dados[:])
    dados.clear()

    answer = str(input('Do you want to continue? [S/N] '))
    if answer in 'Nn':
        break

maior_peso = menor_peso = pessoas[0][1]

print(f'You registered {len(pessoas)} pessoas.')

for p in pessoas:
    if p[1] > maior_peso:
        maior_peso = p[1]
    if p[1] < menor_peso:
        menor_peso = p[1]

print(f'O maior peso foi de {maior_peso} Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')

print()

print(f'O menor peso foi de {menor_peso} Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
