def escreva(msg):
    esp = len(msg) + 2
    print('-' * esp)
    print(f'{msg:^{esp}}')
    print(f'-' * esp)


# Programa Principal
txt = input('Digite uma menssagem: ').strip()
escreva(txt)
