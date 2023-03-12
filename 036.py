casa = float(input())
salario = float(input())
anos = int(input())

mensalidade = casa / (anos * 12)

if mensalidade > (30 / 100) * salario:
    print('O empréstimo foi NEGADO')

else:
    print('O empréstimo foi APROVADO') 