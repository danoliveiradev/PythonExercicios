from random import choice
from time import sleep
print('-=-'*20)
print('\033[91mGAME: JOKENPÔ 👊 🤚 ✌\033[m')
print('-=-'*20)
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
print('''\033[34mOPÇÕES:\033[m
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-=-'*20)
jogador = int(input('Digite o número correspondente a sua jogada (0, 1 ou 2): '))
if 0 <= jogador <= 2:
    maquina = choice(jokenpo)
    print('\033[92mJO\033[m')
    sleep(1)
    print('\033[95mKEN\033[m')
    sleep(1)
    print('\033[96mPÔ!!!\033[m')
    print('-=-'*20)
    print('\033[93mJogador [ {} ] X [ {} ] Máquina\033[m'.format(jokenpo[jogador], maquina))
    #Empate
    if jokenpo[jogador] == maquina:
        print('\033[97mEMPATE! NINGUÉM GANHOU A RODADA.\033[m')
    #Vitória do jogador
    elif jokenpo[jogador] == 'PEDRA' and maquina == 'TESOURA':
        print('\033[92mPARABÉNS! VOCÊ GANHOU DA MÁQUINA.\033[m')
    elif jokenpo[jogador] == 'PAPEL' and maquina == 'PEDRA':
        print('\033[92mPARABÉNS! VOCÊ GANHOU DA MÁQUINA.\033[m')
    elif jokenpo[jogador] == 'TESOURA' and maquina == 'PAPEL':
        print('\033[92mPARABÉNS! VOCÊ GANHOU DA MÁQUINA.\033[m')
    #Vitória da máquina
    elif jokenpo[jogador] == 'PEDRA' and maquina == 'PAPEL':
        print('\033[91mVOCÊ PERDEU PARA A MÁQUINA!\033[m')
    elif jokenpo[jogador] == 'PAPEL' and maquina == 'TESOURA':
        print('\033[91mVOCÊ PERDEU PARA A MÁQUINA!\033[m')
    elif jokenpo[jogador] == 'TESOURA' and maquina == 'PEDRA':
        print('\033[91mVOCÊ PERDEU PARA A MÁQUINA!\033[m')
else:
    print('JOGADA INVÁLIDA! TENTE NOVAMENTE.')