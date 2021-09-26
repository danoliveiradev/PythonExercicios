gols = []
nome = input('Nome do Jogador: ').capitalize().strip()
totalJogos = int(input(f'Quantas partidas {nome} jogou? '))
if totalJogos > 0:
    for g in range(0, totalJogos):
        gols.append(int(input(f'Quantos gols na partida {g}? ')))
aprovJogador = {'nome': nome, 'gols': gols, 'total': totalJogos}
print('-='*30)
print(aprovJogador)
print('-='*30)
for k, v in aprovJogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {aprovJogador["nome"]} jogou {aprovJogador["total"]} partidas.')
for p in range(0, aprovJogador['total']):
    print(f'{"=>":>5} Na partida {p}, fez {aprovJogador["gols"][p]} gols.')
print(f'Foi um total de {sum(aprovJogador["gols"])} gols.')
