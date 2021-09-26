def notas(* n, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos
    :param n: um ou mais notas dos alunos (aceita várias)
    :param sit: (opcional) indica se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre o desempenho da turma
    """
    desempenho = {}
    total = len(n)
    maior = max(n)
    menor = min(n)
    media = sum(n) / len(n)
    if media >= 7:
        situacao = 'BOM'
    elif 6 < media < 7:
        situacao = 'RAZOÁVEL'
    else:
        situacao = 'RUIM'
    desempenho['total'] = total
    desempenho['maior'] = maior
    desempenho['menor'] = menor
    desempenho['media'] = media
    if sit:
        desempenho['situacao'] = situacao
    return desempenho


# Programa Principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)
