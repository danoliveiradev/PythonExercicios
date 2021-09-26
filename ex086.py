matriz = []
valor = []
# ou matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        valor.append(int(input(f'Digite um valor para [{x}, {y}]: ')))
    matriz.append(valor[:])
    valor.clear()
print('-='*30)
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^6}]', end='')
    print()
