kmh = float(input('Quantos Km/h? '))

if kmh > 80:
    multa = (kmh - 80) * 7
    print(f'Você foi multado por ultrapassar o limite de velocidade. Sua multa é de R$ clea{multa:.2f}')

else:
    print('Você está no limite permitido.')