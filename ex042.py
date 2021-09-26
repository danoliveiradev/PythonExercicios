print('-=-'*20)
print('\033[33mANALISADOR DE TRIÂNGULOS\033[m')
print('-=-'*20)
a = float(input('Digite o valor da primeira reta: '))
b = float(input('Digite o valor da segunda reta: '))
c = float(input('Digite o valor da terceira reta: '))
cond1 = (b - c) < a < (b + c)
cond2 = (a - c) < b < (a + c)
cond3 = (a - b) < c < (a + b)
if cond1 and cond2 and cond3:
    if a == b == c:
        print('As retas {}, {}, {} PODEM formar um triângulo do tipo: \033[94mEQUILÁTERO\033[m'.format(a, b, c))
    elif a != b != c != a:
        print('As retas {}, {}, {} PODEM formar um triângulo do tipo: \033[94mESCALENO\033[m'.format(a, b, c))
    else:
        print('As retas {}, {}, {} PODEM formar um triângulo do tipo: \033[94mISÓSCELES\033[m'.format(a, b, c))
else:
    print('\033[31mAs retas {}, {}, {} NÃO podem formar um triângulo.\033[m'.format(a, b, c))
