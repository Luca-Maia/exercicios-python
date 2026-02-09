jogador = dict()

jogador['nome'] = str(input('Nome: '))

partidas = int(input('Partidas jogadas: '))
gols = []

for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))

jogador['gols'] = gols

jogador['total'] = sum(gols)

print('=-' * 30)
print(jogador)

print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i in range(partidas):
    print(f'\t-> Na partida {i}, fez {gols[i]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
