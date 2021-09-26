matriz = []
valor = []
somaPar = somaColuna3 = maiorLinha2 = 0
#Gerador de matriz 3x3
for i in range(0, 3):
    for j in range(0, 3):
        valor.append(int(input(f'Digite um valor para [{i}, {j}]: ')))
    matriz.append(valor[:])
    valor.clear()
print('-='*30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='') #Imprime a matriz 3x3
        if matriz[i][j] % 2 == 0: #Análise soma dos pares
            somaPar += matriz[i][j]
        if j == 2: #Análise soma terceira coluna
            somaColuna3 += matriz[i][j]
        if i == 1: #Análise maior valor linha 2
            if maiorLinha2 <= matriz[i][j]:
                maiorLinha2 = matriz[i][j]
    print()
print('-='*30)
print(f'Soma de todos os valores pares é {somaPar}.')
print(f'Soma dos valores da terceira coluna é {somaColuna3}.')
print(f'O maior valor da segunda linha é {maiorLinha2}.')
