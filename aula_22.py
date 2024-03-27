print('Operadores logicos or(ou)')

"""
And (e) or (or) not (nao)
and - todas as condicoes precisam ser verdadeiras.
Se qualquer valor for considerado falso,
a expressao inteira sera avaliada naquele valor
Sao considerados Falsy (que voce ja viu ) 0, 0.0 , '' False
Tambem existe o tipo None que usado para representar um valor

"""

entrada = input('[E]ntrar [S]air:')
password = input('Pass:')

check_password = '123456'

if (entrada == 'E' or entrada=='e') and check_password ==password:
     print('Entrar')
else:
    print('Sair')


