sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0] #pega só a primeira letra
    if sexo == 'M':
        print('Sexo \033[34mMasculino\033[m registrado com sucesso.')
    elif sexo == 'F':
        print('Sexo \033[35mFeminino\033[m registrado com sucesso.')
    else:
        print('Opção invalida! Tente novamente.')
