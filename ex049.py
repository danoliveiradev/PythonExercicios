num = int(input('Digite um número para ver sua tabuada: '))
print('-=-'*15)
for c in range(0, 11):
    print('{} i {:2} = {}'.format(num, c, num*c))
print('-=-'*15)
