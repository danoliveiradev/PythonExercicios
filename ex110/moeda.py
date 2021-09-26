def metade(v=0, formato=True):
    """
    -> Função que calcula a metade de um valor
    :param v: recebe o valor
    :param formato: recebe verdadeiro ou falso para a formatação do preço (padrão False)
    :return: retorna a metade do valor
    """
    m = v / 2
    return m if formato is False else moeda(m)


def dobro(v=0, formato=True):
    """
    -> Função que calcula o dobro de um valor
    :param v: recebe o valor
    :param formato: recebe verdadeiro ou falso para a formatação do preço (padrão False)
    :return: retorna o o dobro do valor
    """
    m = 2 * v
    return m if formato is False else moeda(m)


def aumentar(v=0, taxa=0, formato=True):
    """
    -> Função que calcula o aumento percentual de um valor
    :param v: recebe valor
    :param taxa: recebe % de aumento
    :param formato: recebe verdadeiro ou falso para a formatação do preço (padrão False)
    :return: retorna o valor aumentado
    """
    m = v + v * taxa / 100
    return m if formato is False else moeda(m)


def diminuir(v=0, taxa=0, formato=True):
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


def resumo(preco=0, aum=10, red=5):
    """
    -> Função que retorna uma tabela que utiliza todas as funcionalidades do módulo moeda
    :param preco:
    :param aum:
    :param red:
    :return:
    """
    print('-' * 30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-' * 30)
    print(f'Preço analisado:\t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco)}')
    print(f'Metade do preço: \t{metade(preco)}')
    print(f'{aum}% de aumento: \t{aumentar(preco, aum)}')
    print(f'{red}% de redução: \t{diminuir(preco, red)}')
    print('-' * 30)
