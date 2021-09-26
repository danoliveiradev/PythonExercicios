print('-=-'*14)
print('{:^40}'.format('BANCO DO LADRÃO'))
print('-=-'*14)
valor = int(input('Quanto deseja sacar? R$'))
total = valor
cedula = 50
totCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totCedula += 1
    else:
        if totCedula > 0:
            print(f'Total de {totCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCedula = 0
        if total == 0:
            break
print('-=-'*14)
print('VOLTE SEMPRE! BANCO DO LADRÃO AGRADECE!')
