'''
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.
'''

numbers = []

r = 'S'

while r != 'N':
    n = int(input('Digite um valor: '))
    if n not in numbers:
        numbers.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = input('Deseja continuar? [S/N] ').upper()

print('=-'*30)

numbers.sort()
print(f'Você digitou os valores {numbers}')