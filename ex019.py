from random import choice
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
escolhido = choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno que irá apagar o quadro será o(a) {}!'.format(escolhido))
