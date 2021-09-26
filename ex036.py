print('\033[34mANALISE DE EMPRÉSTIMO IMOBILIÁRIO\033[m')
valorCasa = float(input('Qual o valor da casa, que você deseja comprar? R$'))
salario = float(input('Quanto é a sua renda? R$'))
anos = int(input('Em quantos anos você deseja parcelar? '))
mensal = valorCasa / (anos * 12)
print('Valor da casa: R${:.2f}\nSalário do comprador: R${:.2f}\nPeríodo de financiamento: {} anos'.format(valorCasa, salario, anos))
print('-=-' * 20)
print('\033[33mANALISANDO SUA PROPOSTA...\033[m')
print('-=-' * 20)
if mensal > (salario * 30/100):
    print('\033[31mEMPRESTIMO NEGADO! Proposta excede 30% da sua renda!\033[m')
else:
    print('\033[32mSOLICITAÇÃO ACEITA!\nForma de pagamento: {} parcelas de R${:.2f}.\033[m'.format(anos * 12, mensal))
