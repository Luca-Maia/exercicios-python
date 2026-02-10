def moeda(valor):
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')



def aumentar(p, percentual, formatar=False):
    if formatar:
        return moeda(p + (p * (percentual / 100)))
    else:
        return p + (p * (percentual / 100))


def diminuir(p, percentual, formatar=False):
    if formatar:
        return moeda(p - (p * (percentual / 100)))
    else:
        return p - (p * (percentual / 100))


def dobro(p, formatar=False):
    if formatar:
        return moeda(p * 2)
    else:
        return p * 2


def metade(p, formatar=False):
    if formatar:
        return moeda(p / 2)
    else:
        return p / 2


def resumo(p, aumento, reducao):
    msg = '        RESUMO DO VALOR        '
    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)

    print(f'{"Preço analisado:":<15}{moeda(p):>10}')
    print(f'{"Dobro do preço:":<15}{dobro(p, True):>10}')
    print(f'{"Metade do preço:":<15}{metade(p, True):>10}')
    #print(f'{f"{aumento}% de aumento:":<10}{aumentar(p, aumento, True):>5}')
    #print(f'{f"{reducao}% de redução:":<10}{diminuir(p, reducao, True):>5}')

    print('-' * tam)
