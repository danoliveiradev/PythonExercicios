from random import randint
from time import sleep
from operator import itemgetter #Busca um item ou items
sorteio = {}
ranking = []
print('-'*30)
print(F'{"VALORES SORTEADOS":^30}')
sleep(1)
for j in range(1, 5):
    sorteio[f'jogador{j}'] = randint(1, 6)
    print(f'O jogador{j} tirou {sorteio[f"jogador{j}"]}')
    sleep(1.2)
print('-'*30)
print(f'{"RANKING DOS JOGADORES":^30}')
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True) #Ordena dicionario em ordem decrescente
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

