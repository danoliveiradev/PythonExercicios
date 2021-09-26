salario = float(input('Qual o seu salário atual? R$'))
nSalario = (salario + salario * 10 / 100 if salario > 1250 else salario + salario * 15 / 100)
print('Parabéns você recebeu um aumento e seu novo salário será R${:.2f}'.format(nSalario))
