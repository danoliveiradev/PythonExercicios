print('-=-'*20)
print('SEQUÊNCIA DE FIBONACCI')
print('-=-'*20)
n = int(input('Quanto termos você quer ver? '))
cont = 2
numAnterior = numPosterior = 0
numAtual = 1
if n == 0:
    print('')
if n == 1:
    print('{}'.format(numAnterior))
elif n >= 2:
    print('{}  {} '.format(numAnterior, numAtual), end='')
    while cont != n:
    #for c in range(2, n, 1):
        numPosterior = numAnterior + numAtual
        numAnterior = numAtual
        numAtual = numPosterior
        print(' {} '.format(numPosterior), end='')
        cont += 1