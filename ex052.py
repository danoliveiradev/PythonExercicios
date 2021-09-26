num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print('O número \033[31m{}\033[m É PRIMO.'.format(num))
else:
    print('O número \033[31m{}\033[m NÃO É PRIMO.'.format(num))
