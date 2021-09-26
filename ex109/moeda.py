def metade(v=0, formato=False):
    """
    -> Função que calcula a metade de um valor
    :param v: recebe o valor
    :param formato: recebe verdadeiro ou falso para a formatação do preço (padrão False)
    :return: retorna a metade do valor
    """
    m = v / 2
    return m if formato is False else moeda(m)


def dobro(v=0, formato=False):
    """
    -> Função que calcula o dobro de um valor
    :param v: recebe o valor
    :param formato: recebe verdadeiro ou falso para a formatação do preço (padrão False)
    :return: retorna o o dobro do valor
    """
    m = 2 * v
    return m if formato is False else moeda(m)


def aumentar(v=0, taxa=0, formato=False):
    """
    -> Função que calcula o aumento percentual de um valor
    :param v: recebe valor
    :param taxa: recebe % de aumento
    :param formato: recebe verdadeiro ou falso para a formatação do preço (padrão False)
    :return: retorna o valor aumentado
    """
    m = v + v * taxa / 100
    return m if formato is False else moeda(m)


def diminuir(v=0, taxa=0, formato=False):
    """
    -> Função que calcula a redução percentual de um valor
    :param v: recebe o valor
    :param taxa: recebe % de redução
    :param formato: recebe verdadeiro ou falso para a formatação do preço (padrão False)
    :return: retorna o valor reduzido
    """
    m = v - v * taxa / 100
    return m if formato is False else moeda(m)


def moeda(v=0, moeda='R$'):
    """
    -> Função que formata os preços no formato moeda
    :param v: recebe preço a ser formatado
    :param moeda: recebe o tipo de moeda (padrão real)
    :return: retorna a o preço formatado
    """
    return f'{moeda}{v:.2f}'.replace('.', ',')
