"""
Formatcao basica de strings 
s - string
f - float
d - int

.<numero de digitos> f

x ou X - Hexadecimal 
(Caractere) (>< ^) (quantidade)

> - Esquerda 
<- Direita
^ - Centro 
= - forca o numero a aparecer antes dos zeros
Sinal - + ou  -
Ex.: ) 0>-100, .1f
Conversion flags - !r = __repre__ , !s = __str__, !a =
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:^10}')
print(f'{1000.123456567:0=+10,.1f}')
print(f'O hexadecimal de 1500 r {1500:08X}')
print(f'{variavel!r}')
