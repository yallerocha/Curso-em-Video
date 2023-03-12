#Primeira forma de resolver:

from random import randint

a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')

x = [a, b, c, d]

print('\nO 1º aluno será {}.\nO 2º aluno será {}.\nO 3º aluno será {}.\nO 4º aluno será {}.'.format(x.pop(randint(0,len(x)-1)), x.pop(randint(0,len(x)-1)), x.pop(randint(0,len(x)-1)), x[0]))

#Segunda forma de resolver:

# from random import choice
#
# a = input('Aluno 1: ')
# b = input('Aluno 2: ')
# c = input('Aluno 3: ')
# d = input('Aluno 4: ')
#
# lista = [a, b, c, d]
#
# A = choice(lista)
# lista.remove(A)
# B = choice(lista)
# lista.remove(B)
# C = choice(lista)
# lista.remove(C)
# D = lista[0]
#
# print('\nO 1º aluno será {}.\nO 2º aluno será {}.\nO 3º aluno será {}.\nO 4º aluno será {}.'.format(A, B, C, D))
