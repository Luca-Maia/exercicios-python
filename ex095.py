jogadores = []

cod = 0

while True:
    dados = {}

    dados['cod'] = cod
    cod += 1

    dados['nome'] = str(input('Nome do jogador: '))

    qtd_partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))

    gols = []
    for i in range(qtd_partidas):
        gols.append(int(input(f'\tQuantos gols na partida {i+1}? ')))

    dados['gols'] = gols

    jogadores.append(dados.copy())
    
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break

print('=-' * 30)
print(f'{"cod":<6}{"nome":<18}{"gols":<20}{"total":>8}')
print('-' * 60)

for j in jogadores:
    print(f'{j["cod"]:<6}{j["nome"]:<18}{str(j["gols"]):<20}{sum(j["gols"]):>8}')
