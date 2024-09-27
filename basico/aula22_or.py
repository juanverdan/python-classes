"""
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senha_permitida = '123'

if entrada == 'E' or senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')
 """

# AVALIAÇÃO DE CURTO CIRCUITO
senha = input('Senha: ') or 'Sem senha'
print(senha)