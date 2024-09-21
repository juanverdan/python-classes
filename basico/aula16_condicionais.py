#if elif else
'''
entrada = input('Você quer entrar ou sair? ')

if entrada == 'entrar':     
    print('Você entrou no sistema')

elif entrada == 'sair':
    print('Você saiu no sistema')

else:
    print('Você não digitou nenhuma das opções') 

'''


#aparentemente, se eu colocar esse int, se eu colocar string, o código nem continua, terei que tomar cuidado!
nota1 = int(input('Qual sua nota 1? '))
nota2 = int(input('Qual sua nota 2? '))
nota3 = int(input('Qual sua nota 3? '))
nota4 = int(input('Qual sua nota 4? '))

nota_geral = (nota1 + nota2 + nota3 + nota4)
print(nota_geral)

if nota_geral < 20:
    print('Você reprovou')

elif nota_geral >= 20:
    print('Parabéns!')

else:
    print('Digite novamente bro')
