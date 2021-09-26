from ex107 import moeda

p = float(input('Digite o preço: R$'))
a = int(input('Digite a % de aumento: '))
d = int(input('Digite a % de redução: '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando {a}%, temos {moeda.aumentar(p, a)}')
print(f'Reduzindo {d}%, temos {moeda.diminuir(p, d)}')
