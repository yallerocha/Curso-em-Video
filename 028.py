import random
numero1 = random.randint(0,5)

numero2 = int(input('Insira um número entre 0 e 5: '))

if numero2 == numero1:
    print('Parabéns! Você ganhou!')
else:
    print('Número errado. Tente novamente!')
 