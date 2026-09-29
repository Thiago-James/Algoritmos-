salário_bruto = float(input('Qual o seu salário: '))

def calcular_imposto_de_renda(Salário):
    if Salário <= 2428.80:
        alg = 0
        impr = 0
    elif Salário <= 2826.65:
        alg = 7.50
        impr = 182.16
    elif Salário <= 3751.05:
        alg = 15.00
        impr = 394.16
    elif Salário <= 4664.68:
        alg = 22.50
        impr = 675.49
    else:
        alg = 27.50
        impr = 908.73

    imposto = ((Salário * alg / 100) - impr)

    return imposto

imposto_novo = calcular_imposto_de_renda(salário_bruto)
print(f'O seu imposto de renda é R$ {imposto_novo :.2f}')
