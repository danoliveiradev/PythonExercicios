from random import randint
numJogador = numComputador = soma = cont = 0
print('-=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR}')
while True:
    print('-=-'*20)
    numJogador = int(input('Digite um valor: '))
    numComputador = randint(0, 10)
    soma = numJogador + numComputador
    opcao = ' '
    while opcao not in 'PI':
        opcao = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {numJogador} e o Computador {numComputador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if opcao == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    elif opcao == 'I':
        if soma % 2 != 0:
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            print('Você PERDEU!')
            break
print('-=-'*20)
print(f'GAME OVER! Você venceu {cont} vezes.')
