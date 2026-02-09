def maior(*nums):
    print('=-' * 30)
    print('Analisando os valores passados...')

    for n in nums:
        print(n, end=' ')

    print(f'Foram informados {len(nums)} valores ao todo.')

    if nums is not ():
        maior = max(nums)
        print(f'O maior valor informado foi {maior}.')
        print('=-' * 30)
        
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
