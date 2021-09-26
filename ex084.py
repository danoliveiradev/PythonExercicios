listaCadastro = []
cadastro = []
maior = 0
while True:
    cadastro.append(input('Nome: ').capitalize().strip())
    cadastro.append(float(input('Peso [Kg]: ')))
    listaCadastro.append(cadastro[:])
    cadastro.clear()
    opcao = input('Deseja continuar [S/N]? ').upper().strip()[0]
    if 'N' in opcao:
        break
print('-='*30)
print(f'Foram cadastradas {len(listaCadastro)} pessoas.')
menor = listaCadastro[0][1]
for p in listaCadastro:
    if p[1] >= maior:
        maior = p[1]
    elif p[1] <= menor:
        menor = p[1]
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in listaCadastro:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in listaCadastro:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
