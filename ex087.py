matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_pares = 0
soma_terceira_coluna = 0

for i in range(0,3):
    for j in range(0,3):
        matriz[i][j] = int(input(f'Digite o valor para a posição [{i}, {j}]: '))
        if i == 0 and j == 0:
            maior_valor_segunda_linha = matriz[i][j]

for i in range(0,3):
    for j in range(0,3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()

for i in range(0,3):
    for j in range(0,3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if j == 2:
            soma_terceira_coluna += matriz[i][j]
        if i == 1:
            if matriz[i][j] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[i][j]


print(f'Soma dos valores pares: {soma_pares}')
print(f'Soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'Maior valor da segunda linha: {maior_valor_segunda_linha}')
