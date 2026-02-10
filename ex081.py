'''
Crie um programa que vai ler vários números e colocar em uma
lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
numbers = list()

while True:
    numbers.append(int(input('Enter a value: ')))
    answer = str(input('Do you want to continue? [S/N] ')).upper()
    if answer == 'N':
        break

print(f'You entered {len(numbers)} values.')

numbers.sort(reverse=True)
print(f'The values in descending order are: {numbers}')

if 5 in numbers:
    print('The value 5 is part of the list.')
else:
    print('The value 5 is not part of the list.')
