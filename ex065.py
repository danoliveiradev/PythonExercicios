from statistics import mean
num = 0
opcao = ''
listaNum = []
while opcao != 'N':
    num = int(input('Digite um número: '))
    listaNum.append(num)
    opcao = input('Deseja continuar? [S/N]: ').upper()[0].strip()
print('Média dos listaValores lidos: {:.2f}'.format(mean(listaNum)))
print('O maior valor lido foi: {}'.format(max(listaNum)))
print('O menor valor lido foi: {}'.format(min(listaNum)))
