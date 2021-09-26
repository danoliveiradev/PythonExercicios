listaAlunos = []
while True:
    nome = (input('Nome: ').capitalize().strip())
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    listaAlunos.append([nome, [nota1, nota2], media])
    opcao = input('Deseja continuar [S/N]? ').upper().strip()[0]
    if 'N' in opcao:
        break
print('-='*30)
print(f'{"No.":5}{"NOME"}{"MÉDIA":>15}')
print('-'*30)
for i, a in enumerate(listaAlunos):
    print(f'{i:<5}{a[0]:16}{a[2]:.1f}')
print('-'*30)
while True:
    aluno = int(input('Mostrar notas de qual aluno [999 interrompe]? '))
    if aluno == 999:
        break
    elif aluno <= len(listaAlunos) - 1:
        print(f'Notas de {listaAlunos[aluno][0]} são {listaAlunos[aluno][1]}')
    else:
        print('No. inválido tente novamente!')
print('FINALIZANDO...')
print('<<<< VOLTE SEMPRE >>>>')
