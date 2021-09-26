from random import randint
from time import sleep
nPC = randint(0, 5)
print('~=~' * 20)
print('Vou pensar em um número entre 0 e 5. Tente Advinhar...')
print('~=~' * 20)
nJ = int(input('Em que número eu pensei? '))
print('PROCESSANDO... ')
sleep(2)
if nPC == nJ:
    print('Você acertou! PARABÉNS! ')
else:
    print('Você errou, eu pensei no número {}!'.format(nPC))
