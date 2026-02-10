'''
Crie um programa que vai ler vários números e colocar em uma
lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas
geradas.
'''

numbers = []
even_numbers = []
odd_numbers = []

while True:
    numbers.append(int(input('Enter a number: ')))
    answer = str(input('Do you want a continue? [S/N] '))
    if answer in 'Nn':
        break

print(f'The complete list is {numbers}')

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    else:
        odd_numbers.append(numbers[i])

print(f'The list of even numbers is {even_numbers}')
print(f'The list of odd numbers is {odd_numbers}')
