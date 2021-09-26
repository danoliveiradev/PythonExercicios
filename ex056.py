from statistics import mean
listaNome = []
listaIdade = []
listaSexo = []
p = 0
for c in range(0, 4):
    p += 1
    #Recebe os dados
    print('====== {}ª PESSOA ====='.format(p))
    nome = input('Nome: ').capitalize().strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    # Lista os dados em Nome, Sexo e Idade
    listaNome.insert(c, nome)
    listaIdade.insert(c, idade)
    listaSexo.insert(c, sexo)
#print('{}\n{}\n{}'.format(listaNome, listaIdade, listaSexo))
#Resposta pergunta 1
print('A média de idade do grupo é: {} anos'.format(int(mean(listaIdade))))
#Filtragem das listas para pergunta 2
filtroSexo = []
filtroIdade = []
#Filtro Sexo
if 'M' in listaSexo:
    for c in range(0, 4):
        if listaSexo[c] == 'M':
            filtroSexo.append(c)
#print(filtroSexo)
#Filtro Idade
    for c in range(1, len(filtroSexo)):
        filtroIdade.append(listaIdade[filtroSexo[c]])
#print(filtroIdade)
#Filtro Nome
    filtroNome = listaNome[listaIdade.index(max(filtroIdade))]
#Resposta pergunta 2
    print('O homem mais velho se chama: {}'.format(filtroNome))
else:
    print('Não existem homens na lista atual.')
#Filtragem das listas para pergunta 3
#Filtro Sexo
n = 0
if 'F' in listaSexo:
    for c in range(0, 4):
        if listaSexo[c] == 'F':
            filtroSexo.append(c)
#Filtro Quantidade (n)
    for c in range(0, len(filtroSexo)):
        if listaIdade[filtroSexo[c]] < 20:
            n = n + 1
    if n > 0:
        print('Nessa lista existe(m) {} mulhere(p) com menos de 20 anos.'.format(n))
    else:
        print('Não existem mulheres com menos de 20 anos na lista atual.')
else:
    print('Não existem mulheres na lista atual.')
