from random import randint
from time import sleep


def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for num in range(0, 5):
        lista.append(randint(0, 10))
        sleep(0.5)
        print(f'{lista[num]} ', end='')
    print('PRONTO!')


def somaPar(valores):
    soma = 0
    for v in valores:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {valores}, temos {soma}')


# Programa Principal
numeros = []
sorteio(numeros)
somaPar(numeros)


