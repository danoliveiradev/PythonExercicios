print('-=-'*20)
print('{:^60}'.format('LOJA DO SUPER BARATA'))
print('-=-'*20)
totCompra = totMil = menorValor = 0
while True:
    opcao = ' '
    produto = input('Nome do Produto: ').strip().capitalize()
    valor = float(input('Preço: R$'))
    totCompra += valor
    if valor > 1000:
        totMil += 1
    if menorValor == 0 or menorValor > valor:
        menorValor = valor
        nomeMenor = produto
    while opcao not in 'SN':
        opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        print('{:^40}'.format('===== FIM DO PROGRAMA ====='))
        break
print(f'O total da compra foi de: R${totCompra:.2f}')
print(f'Temos {totMil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMenor} que custa R${menorValor:.2f}')
