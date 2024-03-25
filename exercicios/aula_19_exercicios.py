print('Exercicio de if e comparacao')

number_1 = int(input('Digite o valor:'))
number_2 = int(input('Digite o valor:'))

if number_1 > number_2:
    print(f'{number_1=}  e maior do que {number_2=}')
elif number_2 > number_1:
    print(f'{number_2=} e maior do que {number_1=}')
else:
    print('sao iguais')