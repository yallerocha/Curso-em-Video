from os import system

system('cls')

#palavra2 = []
#palavra3 = []

frase = input('Digite uma frase: ').strip().lower()
frase2 = frase.split()
frase3 = ''.join(frase2)
inverso = frase3[::-1]

#for i in range(0,len(palavra)):
#    if palavra[i] != " ":
#        palavra2.append(palavra[i])

#for i in range(len(palavra2) - 1, -1, -1):
#    palavra3.append(palavra2[i])

if frase3 == inverso:
    print('É um palíndromo!')

else:
    print('Não é um palíndromo!')