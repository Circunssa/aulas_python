print('formatacao de strings com o metodo format')

a ='A'
b='B'
c=1.1
string = 'a={n}, b={x}, c={y:.2f}'
formato = string.format(n = a,x =b, y=c)#parametro nomeados

print(formato)