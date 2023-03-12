from datetime import date

idades = []
anoatual = date.today().year

for i in range(1,8):
    nascimento = int(input(f'Qual o ano de nascimento da {i}ª pessoa? '))
    idades.append(nascimento)

maiores = 0
menores = 0

for i in idades:
    if anoatual - i < 18:
        menores += 1

    else:
        maiores += 1

print(f'Das 7 pessoas, {menores} são menores e {maiores} são maiores de idade.')
