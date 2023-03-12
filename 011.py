a = float(input('Qual é a largura da parede? '))
b = float(input('Qual é a altura da parede? '))
print('Sua parede tem {:.1f}m².\nVocê irá precisar de {:.1f}l de tinta para pintar a parede.'.format(a*b,a*b/2))