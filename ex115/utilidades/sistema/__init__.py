from time import sleep


def linha(tam=40):
    return '-' * tam


def cor(txt, num=0):
    c = ('\033[m',    # [0] None
         '\033[31m',  # [1] Vermelho
         '\033[32m',  # [2] Verde
         '\033[33m',  # [3] Amarelo
         '\033[34m')  # [4] Azul
    return f'{c[num]}{txt}{c[0]}'


def titulo(txt):
    """
    -> Função que personaliza titulos
    :param txt: recebe o texto a ser personalizado
    :return: sem retorno
    """
    print(linha())
    print(f'{txt:^40}')
    print(linha())


def leiaInt(msg):
    """
    -> Função que só aceita a leitura de números inteiro
    :param msg: recebe texto pedindo um número inteiro
    :return: retorna o resultado na análise
    """
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(cor('ERRO! Por favor, digite um número inteiro válido', 1))
            continue  # Volta ao inicio do while
        else:
            return num


def leiaNome(msg):
    nome = input(msg).strip().title()
    if nome == '':
        nome = 'Desconhecido'
    return nome


def menu(lista):
    sleep(1)
    titulo('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c} -\033[m \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt(cor('Sua opção: ', 2))
    return opc


def lista():
    titulo('PESSOAS CADASTRADAS')
    arquivo = open('listaPessoas.txt', 'r')
    for linha in arquivo:
        print(linha.rstrip())
    arquivo.close()


def cadastro():
    titulo('NOVO CADASTRO')
    nome = leiaNome('Nome: ')
    idade = leiaInt('Idade: ')
    arquivo = open('listaPessoas.txt', 'a')
    arquivo.writelines(f'{nome:<30}{idade} anos\n')
    print(f'Novo registro de <{nome}> adicionado.')
    arquivo.close()


def funcao(opc):
    try:
        if opc == 1:
            lista()
        elif opc == 2:
            cadastro()
        elif opc == 3:
            titulo('Saindo do sistema... Até logo!')
            exit()
        else:
            print(cor('ERRO! Digite uma opção válida', 1))
    except (ValueError, TypeError):
        print(cor('ERRO! Digite uma opção válida', 1))
num = []
