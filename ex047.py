for c in range(1, 51):
    print('.', end='')
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')

#Solução mais rápida e que consome menos iterações
for c in range(2, 51, 2):
    print('.', end='')
    print(c, end=' ')
print('FIM')
