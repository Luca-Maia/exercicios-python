def area():
    print('\tControle de Terrenos')
    print('-' * 35)

    l = float(input('LARGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))

    area = l * c
    print(f'O terreno com as medidas {l} x {c} possui {area} m² de área.')

area()
