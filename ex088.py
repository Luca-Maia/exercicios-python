from random import randint
from time import sleep

lista = list()
jogos = list()

print('-' * 30)
print('           MEGA SENA   ')
print('-' * 30)

qtd_de_jogos = int(input('Quantos jogos serão feitos? '))
total = 1

while total <= qtd_de_jogos:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for c, v in enumerate(jogos):
    print('Sorteando......')
    sleep(1)
    print(f'Jogo {c+1}: {v}')
