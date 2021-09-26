def ficha(n, g):
    """
    ->Programa que mostra a ficha do jogador
    :param n: recebe nome do jogador
    :param g: recebe o número de gols
    :return: retorna msg
    """
    if nome.isalpha() is False:
        n = '<desconhecido>'
    if gols.isnumeric() is False:
        g = 0
    msg = f'O jogador {n} fez {g} gol(s) no campeonato.'
    return msg


# Programa Principal
print('-' * 30)
nome = input('Nome do Jogador: ').capitalize().strip()
gols = input('Número de Gols: ')
print(ficha(nome, gols))
