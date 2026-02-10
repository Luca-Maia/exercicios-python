'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e menor valor digitado e as suas
respectivas posições na lista 
'''

numbers = list()

for i in range(0,5):
    numbers.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior_valor = menor_valor = numbers[i]
    else:
        if numbers[i] > maior_valor:
            maior_valor = numbers[i]
        if numbers[i] < menor_valor:
            menor_valor = numbers[i]

print(f'Você digitou os valoes {numbers}')

print(f'O maior valor digitado foi {maior_valor} nas posições ', end='')
for c, v in enumerate(numbers):
    if v == maior_valor:
        print(f'{c}...', end='')
print()

print(f'O menor valor digitado foi {menor_valor} nas posições ', end='')
for c, v in enumerate(numbers):
    if v == menor_valor:
        print(f'{c}...', end='')
print()
