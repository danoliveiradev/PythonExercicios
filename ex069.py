tot18 = totH = totM20 = 0
while True:
    print('-=-' * 10)
    print('FICHA CADASTRAL')
    print('-=-' * 10)
    sexo = ' '
    opcao = ' '
    idade = int(input('Idade: '))
    if idade >= 18:
        tot18 += 1
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
        if sexo == 'M':
            totH += 1
    if idade < 20 and sexo == 'F':
        totM20 += 1
    print('-'*22)
    while opcao not in 'SN':
        opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        print('\n===== FIM DO PROGRAMA =====')
        break
print(f'\nNúmero de pessoas com mais de 18 anos: {tot18}')
print(f'Número de homens cadastrados: {totH}')
print(f'Número de mulheres com menos de 20 anos: {totM20}')
