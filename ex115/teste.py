from ex115.utilidades import sistema

while True:
    resp = sistema.menu(('Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'))
    sistema.funcao(resp)
