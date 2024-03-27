"""
Peca para o usuario para digitar seu nome e sua idade
Peca para o usuario para digitar sua idade

exiba: 
        Seu nome {Nome} f
        Seu nome invertido e  {Nome_invertido}f
        Seu nome contem (ou nao)  espacos *
        seu nome tem {n} letras f
        A primeira letra do seu nome e {letra}f
        A ultima letra do seu nome e {letra}f
se nada for digitado em seu nome ou idade:f
    exiva "Desculpa, voce deixou campos vazios."
"""
name = input('digita seu nome:')
age = int(input('digita a sua idade:'))

if name  and age:
    for n in name:
        len_name =  len(name)
        text_inverse = name[::-1]
        name_first_word = name[0]
        ultimate =name[-1]

    if ' ' in name:
        print(f'Seu nome contem  espacos')
    else:
        print(' Seu nome contem nao  espacos')

    print(f'Seu nome {name}')
    print(f'Seu nome invertido e  {text_inverse}')
    print(f'A primeira letra do seu nome e {name_first_word}')
    print(f'Seu nome tem {len_name} letras ')
    print(f' A ultima letra do seu nome e {ultimate}')
else:
    print('Desculpa, voce deixou campos vazios.')



