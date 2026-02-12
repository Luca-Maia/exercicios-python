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
    largura = 30
    espaco_valor = 15
    total = largura + espaco_valor

    print('-' * total)
    print('RESUMO DO VALOR'.center(total))
    print('-' *  total)

    print(f'{"Preço analisado:":<{largura}}{moeda(p)}')
    print(f'{"Dobro do preço:":<{largura}}{dobro(p, True)}')
    print(f'{"Metade do preço:":<{largura}}{metade(p, True)}')
    print(f'{f"{aumento}% de aumento:":<{largura}}{aumentar(p, aumento, True)}')
    print(f'{f"{reducao}% de redução:":<{largura}}{diminuir(p, reducao, True)}')

    print('-' * total)