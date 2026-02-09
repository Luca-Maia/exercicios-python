from time import sleep

def contador(i, f, p):
    for n in range(i, f + 1, p):
        print(n, end=' ')
    print(f'FIM !')

print('=-' *  30)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)
print('=-' *  30)

print('=-' *  30)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
print('=-' *  30)
