dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = 60 * dia + 0.15 * km
print('O totCompra a pagar é de \033[1;31mR${:.2f}'.format(total))
