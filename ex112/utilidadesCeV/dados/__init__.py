def leiaDinheiro(msg):
    """
    -> Função que verifica se um preço digitado é valido
    :param msg: recebe a menssagem pedindo um preço
    :return: retorna o preço válido
    """
    while True:
        preco = input(msg).strip().replace(',', '.')
        if preco.isalpha() or preco == "":
            print(f'\033[31mERRO: \"{preco}\" é um preço invalido!\033[m')
        else:
            break
    return float(preco)


def leiaInt(msg):
    """
    -> Função que só aceita a leitura de números
    :param msg: recebe texto pedindo um número
    :return: retorna o resultado na análise
    """
    num = input(msg)
    while num.isnumeric() is False:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        num = input(msg)
    return num