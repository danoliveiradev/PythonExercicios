largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = largura * altura
print('Sua parede tem a dimensão {} i {} e sua área é de {:.2f}m²'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.1f}l de tinta'.format(tinta))
