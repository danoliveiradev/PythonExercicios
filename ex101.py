def voto():
    """
    -> Progrma que recebe o ano de nascimento e informa o satus de obrigatoriedade eleitoral.
    :return: retona menssagem sobre status
    """
    from datetime import  date # Escopo de Importação ( a importação só funciona no def)
    idade = date.today().year - anoNasc
    if 18 <= idade < 65:
        txt = f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade >= 65:
        txt = f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        txt = f'Com {idade} anos: NÃO VOTA.'
    return txt


# Programa Principal
print('-' * 30)
anoNasc = int(input('Em que ano você nasceu? '))
msg = voto()
print(msg)
