jogador = {}
gols = []
time = []
totJogos = 0
while True:
    gols.clear()
    jogador['nome'] = input('Nome: ').capitalize().strip()
    totJogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    if totJogos > 0:
        for p in range(0, totJogos):
            gols.append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = input('Deseja continuar [S/N]? ').upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-'*40)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for i, j in enumerate(time):
    print(f'{i:>3} ', end='')
    for v in j.values():
        print(f'{str(v):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador [999 para parar]? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador para o código {busca}.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for k, v in enumerate(time[busca]['gols']):
            print(f'   ==> Na partida {k+1}, fez {v} gols.')
        print(f'   ==> Foi um total de {sum(time[busca]["gols"])} gols.')
    print('-' * 40)
print('<< ENCERRADO >>')
