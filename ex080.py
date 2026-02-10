'''
Crie um programa onde o usuário possa digitar cinco valores
numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista
ordenada na tela.
'''
numbers = list()

for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > numbers[-1]:
        numbers.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista...')
                break
            pos += 1

print('=-' * 30)
print(f'Os valores digitados em ordem foram {numbers}')
