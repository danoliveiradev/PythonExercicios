print('-=-' * 20)
print('Analisador de Triângulos...')
print('-=-' * 20)
a = float(input('Valor da primeira reta: '))
b = float(input('Valor da segunda reta: '))
c = float(input('Valor da terceira reta: '))
cond1 = (b - c) < a < (b + c)
cond2 = (a - c) < b < (a + c)
cond3 = (a - b) < c < (a + b)
if cond1 and cond2 and cond3:
    print('As retas {}, {} e {} PODEM formar um triângulo'.format(a, b, c))
else:
    print('As retas {}, {} e {} NÃO podem formar um triângulo'.format(a, b, c))
