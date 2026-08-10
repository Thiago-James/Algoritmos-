# Q1
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("A soma é:" , n1 + n2)
print("A subtração é:" , n1 - n2)
print("A multiplicação é:" , n1 * n2)

# Q2
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print("Olá", nome, "você tem", idade, "anos.")

# Q3
numero = float(input('Digite um número: '))

if numero > 0:
    print('O número é positivo.')
elif numero < 0:
    print('O número é negativo.')
else:
    print('O número é zero.')

# Q4

notas = float(input('Digite a nota do aluno:'))

if notas >= 7:
    print('Aprovado')
else:
    print('Reprovado')

# Q5

numero = int(input('Digite um número inteiro: '))

print(f'A tabuada do {numero} é: ')
for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

# Q6

n = int(input('Digite um número inteiro: '))

soma = 0
for i in range(1, n + 1):
    soma += i
print(f'A soma de 1 até {n} é: {soma}')

# Q7

numeros = []
for i in range(1, 11):
    val = float(input(f'Digite o {i}º número: '))
    numeros.append(val)

soma = sum(numeros)
media = soma / len(numeros)

print(f'Soma, {soma}')
print(f'Média, {media}')

# Q8

soma = 0
while True:
    num = float(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    soma += num

print(f"A soma total dos valores digitados é: {soma}")

# Q9

def maior_numero(a, b):
    if a > b:
        return a
    return b

num = float(input("Digite o primeiro número: "))
num = float(input("Digite o segundo número: "))
print(f"O maior número é: {maior_numero(num, num)}")

# Q10

primeiro = float(input("Digite o 1º número: "))
maior = primeiro
menor = primeiro

for i in range(2, 6):
    num = float(input(f"Digite o {i}º número: "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"Maior valor digitado: {maior}")
print(f"Menor valor digitado: {menor}")
