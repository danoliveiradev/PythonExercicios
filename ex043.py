print('-=-'*20)
print('\033[33mCalculadora de IMC\033[m')
print('-=-'*20)
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / pow(altura, 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('\033[97mVocê está ABAIXO DO PESO\033[m')
elif 18.5 <= imc < 25:
    print('\033[92mSeu peso é IDEAL\033[M')
elif 25 <= imc < 30:
    print('\033[93mVocê está com SOBREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[95mVocê está com OBESIDADE\033[m')
else:
    print('\033[91mVocé está com OBESIDADE MÓRBIDA\033[m')