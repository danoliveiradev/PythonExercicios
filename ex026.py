frase = input('Digite uma frase: ').strip().upper()
print('Analisando a frase "{}"'.format(frase))
print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1)) #Iniciar a contagem em 1 (+1)
print('A letra "A" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))
