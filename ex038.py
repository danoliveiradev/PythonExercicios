n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('\033[32mAnalisando os números {} e {}...'.format(n1, n2))
if n1 > n2:
    print('\033[31mO primeiro valor é maior!')
elif n1 < n2:
    print('\033[31mO segundo valor é maior!')
else:
    print('\033[31mNão existe valor maior, os dois são iguais!')