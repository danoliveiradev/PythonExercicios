a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 0
an = a1
print('[ ', end='')
while cont != 10:
    print('{} '.format(an), end='')
    an += r
    cont += 1
print(']')
