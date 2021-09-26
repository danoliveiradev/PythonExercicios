cadastro = {}
pessoas = []
soma = media = 0
while True:
    cadastro['nome'] = input('Nome: ').capitalize()
    while True:
        sexo = input('Sexo [M/F]: ').upper().strip()[0]
        if sexo in 'MF':
            cadastro['sexo'] = sexo
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    pessoas.append(cadastro.copy())
    while True:
        opcao = input('Deseja continuar [S/N]? ').upper().strip()[0]
        if opcao in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if opcao == 'N':
        break
print('-='*30)
print(f'- Foram cadastradas {len(pessoas)} pessoas.')
media = soma / len(pessoas)
print(f'- A média de idade é {media:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if 'F' in p['sexo']:
        print(f'{p["nome"]} ', end='')
print('\n- A lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > media:
        print('    >> ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
