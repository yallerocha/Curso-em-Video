from datetime import date

ano = int(input())
atual = date.today().year

if atual - ano < 18:
    falta = 18 - (atual - ano)
    print(f'Ainda não está no tempo de se alistar, faltam {falta} anos.')

elif atual - ano > 18:
    passou = (atual - ano) - 18
    print(f'Já passou o tempo de se alistar, passaram {passou} anos ')
    
else:
    print('Você deve se alistar neste ano!')