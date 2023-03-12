from os import system

system('cls')

sexo = input('Qual o seu sexo? [M/F]: ').strip().upper()[0]

res = ['M', 'F']

while sexo not in res:
    sexo = str(input('Resposta inválida. Qual o seu sexo? ').strip().upper())

print('Registrado!')