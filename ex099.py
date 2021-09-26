from time import sleep


def maior(* num):
    m = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for v in num:
        if v > m:
            m = v
        sleep(0.5)
        print(f'{v} ', end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {m}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
