listaUnica = [[], []]
for num in range(1, 8):
    valor = int(input(f'Digite o {num}º valor: '))
    if valor % 2 == 0:
        listaUnica[0].append(valor)
    else:
        listaUnica[1].append(valor)
listaUnica[0].sort()
listaUnica[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {listaUnica[0]}')
print(f'Os valores ímpares digitados foram: {listaUnica[1]}')
