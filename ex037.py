print('-=-'*20)
print('\033[31mCONVERSOR DE BASE\033[m')
print('-=-'*20)
num = int(input('Digite um número inteiro: '))
print('''\033[34mBases de conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal\033[m''')
base = int(input('Digite o número correspondente a base selecionada: '))
if base == 1:
    conv = bin(num)[2:]
    print('\033[33mO número {} em binário equivale a {}.'.format(num, conv))
elif base == 2:
    conv = oct(num)[2:]
    print('\033[33mO número {} em octal equivale a {}.'.format(num, conv))
elif base == 3:
    conv = hex(num)[2:]
    print('\033[33mO número {} em hexadecimal equivale a {}.'.format(num, conv))
else:
    print('Opção invalida! Tente novamente.')
