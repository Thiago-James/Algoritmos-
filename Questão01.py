Aluno = input('Qual é o seu nome ?: ')
Notas = []
quants_notas = int(input('Quantas irão ser contabilizadas: '))

for i in range(7):
    notas_válidas = float(input(f'Insira {i + 1} as suas notas: '))
    Notas.append(notas_válidas)

def calcular_média(a, b):
    soma = (a + b) / 2
    return soma

média_aluno = calcular_média(sum(Notas), len(Notas))
print(média_aluno)

if média_aluno >= 8:
    print('APROVADO')
else:
    print('REPROVADO')