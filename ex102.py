def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    
    :param n: O número a ser calculado
    :param show: Mostrar ou não a conta
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

print(fatorial(7, show=True))
help(fatorial)
