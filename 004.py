n=input('Digita alguma coisa aí: ')
print('Tipo Primitivo: {}'.format(type(n)))
print('{}'.format('É alfanumérico?'),n.isalnum())
print('{}'.format('Só tem letras?'),n.isalpha())
print('{}'.format('Está tudo em minúsculo?'),n.islower())
print('{}'.format('Só tem números?'),n.isnumeric())
print('{}'.format('Está tudo em maiúsculo?'),n.isupper())