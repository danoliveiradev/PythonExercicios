listaNum = []
for c in range(0, 5):
    listaNum.append(int(input(f'Digite um número para posição {c}: ')))
print('-=-'*20)
print(f'Você digitou os valores: {listaNum}')
print(f'O maior valor digitado foi {max(listaNum)} nas posições ', end='')
for p, n in enumerate(listaNum):
    if max(listaNum) == n:
        print(f'{p}...', end='')
print(f'\nO menor valor digitado foi {min(listaNum)} nas posições ', end='')
for p, n in enumerate(listaNum):
    if min(listaNum) == n:
        print(f'{p}...', end='')
