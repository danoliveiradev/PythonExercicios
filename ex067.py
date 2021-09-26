while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('='*50)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('='*50)
print('PROGRAMA TABUADA ENCERRADO! VOLTE SEMPRE!')