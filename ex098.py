from time import sleep


def contador(i, f, p):
    print('-=' * 30)
    print(f'Contagem de {i} até {f} de ', end='')
    if f < i:
        f = f - 1
    else:
        f = f + 1
    if p < 0:
        print(f'{p*(-1)} em {p*(-1)}.')
    elif p == 0:
        if i > f:
            p = -1
            print(f'{p*(-1)} em {p*(-1)}.')
        else:
            p = 1
            print(f'{p} em {p}.')
    if p > 0:
        print(f'{p} em {p}.')
        if i > f:
            p *= -1
    for c in range(i, f, p):
        sleep(0.5)
        print(f'{c} ', end='')
    print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
