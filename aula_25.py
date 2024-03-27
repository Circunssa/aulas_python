print('Interpolacao de string com % em python')

"""
Interpolacao de string com % em python
s - string
d e i - int
f - float
x e x - hexadecimal (ABDEF0123456789)

"""

name = 'Fabio'
price  = 1000.95897643
variavel = '%s, o preco total foi de R$%.2f' %(name, price)
print(variavel)
print('O hexadecimal de %d e %04x' % (15,15))