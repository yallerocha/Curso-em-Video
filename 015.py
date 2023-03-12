a = float(input('Quantos Km o carro percorreu? '))
b = int(input('O carro foi alugado por quantos dias? '))
print('Você irá pagar R${:.2f}'.format(60*b+0.15*a))