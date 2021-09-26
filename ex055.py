listaPeso = []
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa em Kg: '.format(c)))
    listaPeso.insert(c, peso)
print('Maior peso: {}Kg'.format(max(listaPeso)))
print('Menor peso: {}Kg'.format(min(listaPeso)))
