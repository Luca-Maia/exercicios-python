from random import randint

numeros = []

def sorteia():
    print('Sorteando 5 valores da lista: ')

    for i in range(0,5):
        n = randint(0,10)
        print(n, end=' ')
        numeros.append(n)
    
    print('PRONTO!')

def sorteiapar(numeros):
    soma_par = 0
    for i in numeros:
        if i % 2 == 0:
            soma_par += i

    print(f'Somando os valores pares de {numeros}, temos {soma_par}')

sorteia()
sorteiapar(numeros)
