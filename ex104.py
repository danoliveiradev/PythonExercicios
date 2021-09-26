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


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
