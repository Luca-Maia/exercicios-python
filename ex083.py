'''
Crie um programa onde o usuário digite uma expressão
qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e
fechados em ordem correta.
'''

expression = (str(input('Enter a expreesion: ')))

stack = list()

for symbol in expression:
    if symbol == '(':
        stack.append('(')
    elif symbol == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('Your expression is valid!')
else:
    print('Your expression is invalid!')
