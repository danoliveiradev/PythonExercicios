velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você ultrapassou o limite de velocidade máxima de 80Km/h \ne deverá pagar uma multa de R${:.2f}'.format(multa))
print('Boa viagem e dirija com segurança!')
