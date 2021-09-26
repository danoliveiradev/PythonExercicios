numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
              'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um valor entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numExtenso[num]}')
        opcao = input('Deseja continuar [S/N]? ').upper().strip()[0]
        if opcao == 'N':
            break
    else:
        print('Tente novamente.', end='')
print('Programa Finalizado!')
