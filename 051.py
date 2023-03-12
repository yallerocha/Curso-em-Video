primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
enezimo = primeirotermo + (10 - 1) * razao

for i in range(primeirotermo,enezimo+razao,razao):
    print(i , end=' ')

print('Acabou')