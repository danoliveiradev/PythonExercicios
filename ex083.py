calculo = input('Digite uma expressão matemática: ').strip()
if calculo.count('(') == calculo.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
