listaValores = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
                int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))
print(f'Você digitou os valores: {listaValores}')
print(f'O valor 9 apareceu {listaValores.count(9)} vezes.')
if 3 in listaValores:
    print(f'O valor 3 apareceu pela primeira vez na {listaValores.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('É par: ', end='')
for n in listaValores:
    if n % 2 == 0:
        print(f'{n} ', end='')
