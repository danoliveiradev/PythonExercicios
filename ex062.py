a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
contTermos = 10
mais = 1
an = a1
while mais != 0:
    if c != contTermos:
        print('{} '.format(an), end='')
        an += r
        c += 1
    elif c == contTermos:
        mais = int(input('\nDeseja contar mais quantos termos? '))
        contTermos += mais
print('A progressão foi finalizada com {} termos contados'.format(contTermos))
