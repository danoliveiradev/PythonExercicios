print('==============LOJAS OLIVEIRA==============')
totCompra = float(input('Digite o valor da compra em R$'))
print('-=-'*20)
print('''\033[31mFORMAS DE PAGAMENTO\033[m)
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print('-=-'*20)
opcao = int(input('Selecione o número correspondente a opção de pagamento (1, 2, 3 ou 4): '))
if opcao == 1:
    pFinal = totCompra - (totCompra * 10 / 100)
    print('Sua compra que custava R${:.2f} vai custar R${:.2f} no final.'.format(totCompra, pFinal))
elif opcao == 2:
    pFinal = totCompra - (totCompra * 5 / 100)
    print('Sua compra que custava R${:.2f} vai custar R${:.2f} no final.'.format(totCompra, pFinal))
elif opcao == 3:
    pFinal = totCompra
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(totCompra / 2))
elif opcao == 4:
    pFinal = totCompra + (totCompra * 20 / 100)
    nParcelas = int(input('Quantas parcelas? '))
    if nParcelas > 2:
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(nParcelas, pFinal / nParcelas))
        print('Sua compra que custava R${:.2f} vai custar R${:.2f} no final.'.format(totCompra, pFinal))
    else:
        print('Opção invalida! Tente novamente.')
else:
    print('Opção invalida! Tente novamente.')
