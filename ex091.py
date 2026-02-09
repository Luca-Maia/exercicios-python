from random import randint
from time import sleep

jogadores = dict()

for i in range(0,4):
    jogadores[f'Jogador {i}'] = randint(1,6)

print('Valores sorteados: ')

for k, v in jogadores.items():
    sleep(1)
    print('....Jogando dados...')
    sleep(1)
    print(f'{k} tirou {v} nos dados')

ranking_jogadores = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

print('Ranking dos jogadores: ')

for k, v in ranking_jogadores.items():
    print(f'{k} com {v}')

