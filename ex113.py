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
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
            continue #Volta ao inicio do while
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    """
    -> Função que só aceita a leitura de números reais
    :param msg: recebe texto pedindo um número real
    :return: retorna o resultado na análise
    """
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


# Programa Principal
i = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {i} e o real {r}')
