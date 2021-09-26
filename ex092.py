from datetime import date
cadastro = {}
cadastro['nome'] = input('Nome: ').capitalize().strip()
anoNasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = date.today().year - anoNasc
cadastro['ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))
if cadastro['ctps'] != 0:
    cadastro['anoContr'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (cadastro['anoContr'] + 35) - anoNasc
print('-='*20)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
