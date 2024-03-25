print('Precedencia entre os operadores aritmeticos')
# 1. (n+n)
# 2.  **
# 3. * / // % <- executa da esquerda para direita
# 4. + -

conta_1 = 1+ 1 ** 5+5
conta_2 = (1+ 1) **( 5+5)
conta_3 = (1+ int(0.5 + 0.5))** 5+5
conta_4 = int(1+ (0.5 + 0.5)) ** (5+5)
print(conta_1)
print(conta_2)
print(conta_3)
print(conta_4)