frase = input('Digite uma frase: ').upper().strip()
print('A frase: \033[31m{}\033[m'.format(frase))
juntaString = frase.replace(' ', '')
reverteString = juntaString[::-1]
''' ou
for letra in range(len(juntaString) -1, -1, -1):
    reverteString += juntaString[letra]'''
if juntaString == reverteString:
    print('É um PALÍNDROMO!')
else:
    print('NÃO é um PALÍNDROMO!')
