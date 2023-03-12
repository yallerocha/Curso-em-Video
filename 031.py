distancia = float(input('Qual é a distância em Km? '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor da passagem é de R$ {valor:.2f}')

else:
    valor = distancia * 0.45
    print(f'O valor da passagem é de R$ {valor:.2f}')