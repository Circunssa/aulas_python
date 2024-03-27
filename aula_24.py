print('Operadores in e not in ')
"""
Operadores in e not in 
String sao iteraveis
0 1 2 3 4 5
F A B i O
-5 -4 -3 -2 -1 
"""

name = 'Fabio'
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[-5])
print(10 * '->')
print('i' in name)

print('bio ' not in name)

name_user = input('Digit your name:')
encontrar = input('digit o que quer encontrar:')

if encontrar in name:
    print(f'{encontrar} esta em {name_user}')
else:
    print(f'{encontrar} nao esta em {name_user}')