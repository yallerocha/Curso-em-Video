from math import hypot
a = float(input('Qual o comprimento do cateto oposto? '))
b = float(input('Qual o comprimento do cateto adjacente? '))
print('A hipotenusa desse triângulo retângulo é {:.2f}'.format(hypot(a, b)))
