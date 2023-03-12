from random import choice

a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')

nomes = [a, b, c, d]

print('\nO aluno selecionado foi {}.'.format(choice(nomes)))
