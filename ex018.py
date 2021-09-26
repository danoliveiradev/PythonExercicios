from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo em graus: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print('Para o ângulo {}º: \nseno = {:.3f} \ncosseno = {:.3f} \ntangente = {:.3f}'.format(angulo, seno, coss, tang))
