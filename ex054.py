from datetime import date
listaMaior = []
listaMenor = []
for c in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - nasc
    if idade <= 21:
        listaMenor.append(nasc)
    else:
        listaMaior.append(nasc)
listaMenor.sort()
listaMaior.sort()
if listaMenor == []:
    print('NÃO HOUVE MENORES DE IDADE.')
else:
    print('SÃO {} MENORES DE IDADE. NASCIDOS EM: {}.'.format(len(listaMenor), listaMenor))
if listaMaior == []:
    print('NÃO HOUVE MAIOREs DE IDADE.')
else:
    print('SÃO {} MAIORES DE IDADE. NASCIDOS EM: {}.'.format(len(listaMaior), listaMaior))
