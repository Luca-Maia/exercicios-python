numbers = [[], []]
temp = 0

for i in range(0,7):
    temp = int(input(f'Enter a {i+1}o. value: '))
    if temp % 2 == 0:
        numbers[0].append(temp)
    else:
        numbers[1].append(temp)

print('=-' * 30)

numbers[0].sort()
numbers[1].sort()

print(f'Os valores pares digitados foram {numbers[0]}')
print(f'Os valores ímpares digitados foram {numbers[1]}')
