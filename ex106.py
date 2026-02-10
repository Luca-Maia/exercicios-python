def ajuda(comando):
    help(comando)


# Programa principal
comando = ''
while True:
    comando = str(input('Função ou Biblioteca: '))
    if comando.strip().upper() == 'FIM':
        break
    else:
        ajuda(comando)
