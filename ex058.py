from random import randint
numComputador = randint(0, 10)
numJogador = -1
tentativas = 0
print('-=-' *20)
print('\033[34mPENSEI EM UM NÚMERO INTEIRO ENTRE 0 e 10. TENTE ADIVINHAR\033[m')
print('-=-'*20)
while numJogador != numComputador:
    numJogador = int(input('Advinhe o número: '))
    tentativas += 1
    if numJogador > numComputador:
        print('\033[31mMenos... Tente novamente.\033[m')
    elif numJogador < numComputador:
        print('\033[31mMais... Tente novamente.\033[m')
print('\033[32mParabéns você acertou!\033[m')
print('Foram necessários {} tentativas até você acertar.'.format(tentativas))
