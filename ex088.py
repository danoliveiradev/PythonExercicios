from random import sample
from time import sleep
listaJogos = []
jogo = []
print('-'*60)
print(f'{"JOGO NA MEGA SENA":^60}')
print('-'*60)
cont = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-=-=-= SORTEANDO {cont} JOGOS =-=-=-=-=-=-')
for j in range(1, cont+1):
    jogo.append(sample((range(1, 61)), 6))
    jogo[0].sort()
    listaJogos.append(jogo[:])
    jogo.clear()
    sleep(1)
    print(f'Jogo {j}: {listaJogos[j-1]}')
sleep(1)
print('-=-=-=-=-=-= BOA SORTE! =-=-=-=-=-=-')
