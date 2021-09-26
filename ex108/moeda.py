def metade(v=0):
    """
    -> Função que calcula a metade de um valor
    :param v: recebe o valor
    :return: retorna a metade do valor
    """
    m = v / 2
    return m


def dobro(v=0):
    """
    -> Função que calcula o dobro de um valor
    :param v: recebe o valor
    :return: retorna o o dobro do valor
    """
    m = 2 * v
    return m


def aumentar(v=0, taxa=0):
    """
    -> Função que calcula o aumento percentual de um valor
    :param v: recebe valor
    :param taxa: recebe % de aumento
    :return: retorna o valor aumentado
    """
    m = v + v * taxa / 100
    return m


def diminuir(v=0, taxa=0):
    """
    -> Função que calcula a redução percentual de um valor
    :param v: recebe o valor
    :param taxa: rece % de redução
    :return: retorna o valor reduzido
    """
    m = v - v * taxa / 100
    return m


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
