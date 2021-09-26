"""
distancia = float(input('Qual a distância da sua viagem em Km? '))
if distancia <= 200:
    pViagem = distancia * 0.50
    print('O preço da sua passagem para a distância de {}Km será de R${:.2f}'.format(distancia, pViagem))
else:
    pViagem = distancia * 0.45
    print('O preço da sua passagem para a distância de {}Km será de R${:.2f}'.format(distancia, pViagem))
"""
distancia = float(input('Qual a distância da sua viagem? '))
pViagem = (distancia * 0.50 if distancia <= 200 else distancia * 0.45)
print('O preço da sua passagem para a distância de {}Km será de R${:.2f}'.format(distancia, pViagem))
