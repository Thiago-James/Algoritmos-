Peso = float(input('Fale o quanto está pesando no momento: '))
Altura = float(input('Fale quanto está de altura no momento: '))

IMC = Peso / (Altura * Altura)

print(f'Seu IMC é: {IMC :.2f}')

if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC <= 25.0:
    print('PESO NORMAL')
elif IMC <= 30.0:
    print('SOBREPESO')
else:
    print('OBESIDADE')


