from datetime import date
anoNasc = int(input('Digite seu ano de nascimento com 4 digitos: '))
idade = date.today().year - anoNasc
if idade < 18:
    print('\033[32mVocê não completou 18 anos! Vai poder se alistar daqui a {} anos.'.format(18 - idade))
elif idade == 18:
    print('\033[33mVocê completou 18 anos! Procure um junta militar para se alistar.')
elif idade > 18:
    print('\033[31mVocê tem mais de 18 anos e passou do período de alistamento a {} anos.'.format(idade - 18))
    print('CASO NÃO TENHA SE ALISTADO, PROCURE A JUNTA MILITAR MAIS PRÓXIMA!')