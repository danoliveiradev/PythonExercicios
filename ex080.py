'''
num = int(input('Digite um valor: '))
listaNum = [num]
print('Adicionado na posição 0 da lista...')
for cont in range(1, 5):
    num = int(input('Digite um valor: '))
    if num <= min(listaNum):
        listaNum.insert(0, num)
        print('Adicionado na posição 0 da lista...')
    elif num >= max(listaNum):
        listaNum.append(num)
        print('Valor adicionado ao final da lista...')
    elif min(listaNum) < num < max(listaNum):
        for i in range(0, 3):
            if listaNum[i] < num <= listaNum[i+1]:
                listaNum.insert(i+1, num)
                print(f'Valor adicionado a posição {i+1} da lista')
print('-=-'*20)
print(f'Os valores digitados foram {listaNum}')
'''
#Curso em Video
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado a posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valors digitados em ordem foram {lista}')
