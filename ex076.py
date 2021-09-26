listaProdutos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
                 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-=-'*20)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('-=-'*20)
for c in range(0, len(listaProdutos), 2):
    print(f'{listaProdutos[c]:.<50}'+f'R${listaProdutos[c+1]:>7.2f}')
print('-=-'*20)
