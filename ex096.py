def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.1f}m².')


# Programa Principal
print(f'{"CONTROLE DE TERRENO":^30}')
print('-'*30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
