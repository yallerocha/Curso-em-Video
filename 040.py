nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2) / 2
print(f'Sua nota é {media:.1f}')
if media >= 7:
    print('Aprovado')

elif 5 <= media < 7:
    print('Recuperação')

else:
    print('Reprovado')
