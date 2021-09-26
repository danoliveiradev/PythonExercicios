tabCampBrasileiro = ('Fortaleza', 'Athletico-PR', 'Bragantino', 'Flamengo', 'Atlético-GO', 'Atlético-MG', 'Bahia',
                     'Palmeiras', 'Fluminense', 'Corinthians', 'Ceará SC', 'Santos', 'Internacional', 'Juventude',
                     'Cuiabá', 'Sport Recife', 'São Paulo', 'Chapecoense', 'Grêmio', 'América-MG')
print(f'Lista de times Brasileirão: {tabCampBrasileiro}')
print('='*40)
print(f'Os 5 primeiros colocados: {tabCampBrasileiro[0:5]}')
print('='*40)
print(f'Os 4 últimos colocados: {tabCampBrasileiro[-4:]}')
print('='*40)
print(f'Lista de Times em Ordem Alfabética: {sorted(tabCampBrasileiro)}')
print('='*40)
posicao = tabCampBrasileiro.index('Chapecoense')
print(f'A Chapecoense está na {posicao + 1}ª posição')
