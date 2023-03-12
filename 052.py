from os import system

system('cls')

div = []
cont = 0

num = int(input('Digite um número: '))

for i in range(1,num + 1):
    if num % i  == 0:
        div.append(i)
        cont += 1

print()
if len(div) == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo, pois ele foi divisivel {cont} vezes.')