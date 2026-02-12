def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            return valor
