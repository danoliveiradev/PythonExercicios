nome = input('Qual o seu produto completo? ').strip().upper()
print('Prazer em te conhecer {}'.format(nome))
print('Seu primeiro produto é {}'.format(nome.split()[0]))
print('Seu último produto é {} \nEsta correto?'.format(nome.split()[len(nome.split()) - 1]))

