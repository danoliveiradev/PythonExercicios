from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;97;41m',   # 1 - vermelho
     '\033[0;97;42m',   # 2 - verde
     '\033[0;97;43m',   # 3 - amarelo
     '\033[0;97;44m',   # 4 - azul
     '\033[0;97;45m',   # 5 - roxo
     '\033[1;30;107m'   # 6 - branco
     )


def titulo(txt, cor=0):
    """
    -> Função que personaliza titulos e texto
    :param txt: recebe o texto ou titulo a ser personalizado
    :param cor: recebe a cor desejada através da tupla c
    :return: sem retorno
    """
    tam = len(txt) + 2
    print(f'{c[cor]}', end='')
    print(f'-' * tam)
    print(f'{txt:^{tam}}')
    print('-' * tam)
    print(f'{c[0]}', end='')
    sleep(1)


def pyHelp(com):
    """
    Função de sistema de ajuda do Python personalizado
    :param com: recebe o a função ou biblioteca a ser consultada
    :return: sem retorno
    """
    titulo(f'ACESSANDO O MANUAL DO COMANDO \'{com}\'', 2)
    print(f'{c[6]}', end='')
    help(com)
    print(f'{c[0]}', end='')
    sleep(1)


# Programa Principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 4)
    ajuda = input('Função ou Biblioteca: ').lower().strip()
    if ajuda in 'fim':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        pyHelp(ajuda)
