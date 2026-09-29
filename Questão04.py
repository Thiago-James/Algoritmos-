Salário = float(input('Insira seu salário: '))
Bonif = float(input('Insira aqui sua bonificação em porcentagem '))

def calcular_bonificação(taxa_bonus, salário_base):
    salário_base = Salário
    taxa_bonus = ((Bonif * Salário) / 100)

    return salário_base + taxa_bonus

Salário_inteiro = calcular_bonificação(Bonif, Salário)

print(f'Salário Base é {Salário}')
print(f'Salário atualizado a sua bonificação: R${Bonif}')
