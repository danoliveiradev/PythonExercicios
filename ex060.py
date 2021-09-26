num = int(input('Digite um número: '))
cont = num
fatorial = 1
print('{}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' i ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
'''
#Utilizando for
for c in range(valor, 0, -1):
    print('{}'.format(c), end='')
    print(' i ' if c > 1 else ' = ', end='')
    fatorial *= c
'''
print('{}'.format(fatorial))
