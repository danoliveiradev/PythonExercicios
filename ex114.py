import urllib.request

try:
    resp = urllib.request.urlopen("http://www.pudim.com.br").getcode()
except:
    print('\033[31mO site Pudim não está acessível no momento!\033[m')
else:
    print('\033[92mConsegui acessar o site Pudim com sucesso!\033[m')
