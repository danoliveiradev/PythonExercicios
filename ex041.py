from datetime import date
print('-=-'*20)
print('\033[93mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('-=-'*20)
anoNasc = int(input('Digite o ano de seu nascimento, com 4 digitos: '))
idade = date.today().year - anoNasc
if idade <= 9:
    print('De acordo com a sua idade sua categoria é: \033[32mMIRIM')
elif 9 < idade <= 14:
    print('De acordo com a sua idade sua categoria é: \033[34mINFANTIL')
elif 14 < idade <= 19:
    print('De acordo com a sua idade sua categoria é: \033[33mJUNIOR')
elif 19 < idade <= 25:
    print('De acordo com a sua idade sua categoria é: \033[97mSÊNIOR')
elif idade > 25:
    print('De acordo com a sua idade sua categoria é: \033[31mMASTER')
