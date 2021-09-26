a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + (10 - 1) * r
print('[ ', end='')
for c in range(a1, a10 + r, r):
    print('{}'.format(c), end=' ')
print(']', end='')
