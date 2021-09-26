n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('-=-' * 10)
    print('''Menu de opções:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    print('-=-' * 10)
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        print('A soma {} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação {} i {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        print('O maior número entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == 5:
        print('Programa finalizado!')
    else:
        print('Opção invávilda! Tente Novamente.')
