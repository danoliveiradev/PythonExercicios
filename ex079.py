listaNum = []
while True:
    num = int(input('Digit um valor: '))
    if num not in listaNum:
        listaNum.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if opcao == 'N':
        break
print('-=-'*20)
listaNum.sort()
print(f'Você digitou os valores: {listaNum}')
