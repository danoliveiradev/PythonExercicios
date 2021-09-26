listaNum = []
listaPar = []
listaImpar = []
while True:
    listaNum.append(int(input('Digite um valor: ')))
    opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if opcao == 'N':
        break
print('='*60)
for num in listaNum:
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
print(f'Lista completa: {listaNum}')
print(f'Lista de pares: {listaPar}')
print(f'Lista de ímpares: {listaImpar}')
