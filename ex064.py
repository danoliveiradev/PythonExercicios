n = cont = soma = 0
while n != 999: #999 é o "flag"
    n = int(input('Digite um número [999 para PARAR]: '))
    if n != 999:
        soma += n
        cont += 1
print('Números digitados: {}\nSoma Total = {}'.format(cont, soma))
