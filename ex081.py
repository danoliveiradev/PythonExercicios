listaNum = []
while True:
    listaNum.append(int(input('Digite um número: ')))
    opcao = input('Deseja continuar? [S/N]').upper().strip()[0]
    if opcao == 'N':
        break
print('='*40)
print(f'Foram digitados {len(listaNum)} elementos')
listaNum.sort(reverse=True)
print(f'Lista de elementos em ordem decrescente: {listaNum}')
if 5 in listaNum:
    print('O número 5 aparece na lista, nas posições ', end='')
    for pos, num in enumerate(listaNum):
        if num == 5:
            print(f'{pos}...', end='')
else:
    print('O número 5 não está na lista.')