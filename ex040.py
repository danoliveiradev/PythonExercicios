n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
print('Sua média é {:.1f}\nDe acordo com a sua média:'.format(med))
if med < 5:
    print('Você está \033[31mREPROVADO')
elif 5 <= med <= 6.9:
    print('Você está em \033[33mRECUPERAÇÃO')
else:
    print('Parabéns! Você está \033[32mAPROVADO')
