from ex109 import moeda

p = float(input('Digite o preço: R$'))
a = int(input('Digite a % de aumento: '))
d = int(input('Digite a % de redução: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando {a}%, temos {moeda.aumentar(p, a, True)}')
print(f'Reduzindo {d}%, temos {moeda.diminuir(p, d, True)}')
