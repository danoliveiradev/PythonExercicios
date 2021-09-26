from random import randint
listaNum = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in range(0, len(listaNum)):
    print(f'{listaNum[n]} ', end='')
print(f'\nO maior valor sorteado foi: {max(listaNum)}')
print(f'O menor valor sorteado foi: {min(listaNum)}')
