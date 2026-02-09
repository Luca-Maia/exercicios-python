from datetime import date

def voto(ano_de_nascimento):
    # Calcular a idade
    hoje = date.today()
    idade = hoje.year - ano_de_nascimento
    
    # Classificar o voto (opcional, obrigatório, negado)
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif (16 <= idade < 18) or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

print('-' * 30)
while True:
    ano = int(input('Em que ano você nasceu? '))
    if date.today().year > ano >= 1906:
        break
    else:
        print('Ano de nascimento inválido. Tente novamente.')  

print(voto(ano))
