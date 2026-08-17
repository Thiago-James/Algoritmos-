# Aluno: Thiago
# Matrícula: 202613187

# 1 Questão 

numeros = [10, 20, 30, 40, 50]

print("Primeiro:", numeros[0])
print("Terceiro:", numeros[2])
print("Último:", numeros[-1])
print("Quantidade de elementos:", len(numeros))

# 2 Questão

Numeros = [7, 12, 5, 18, 3, 20]

print('Todos os elementos:')
for num in Numeros:
    print(num)

print('Maiores que 10:')
for num in Numeros:
    if num > 10: 
        print(num)

# 3 Questão

Numeros = [4, 7, 2, 9, 15, 1, 8, 3]

Soma = 0 
for num in Numeros:
    Soma += num 

print('Soma total:', Soma)

# 4 Questão

Notas = [7.5, 8.0, 6.0, 9.5, 5.5]

Soma = 0
Quantidade = 0

for nota in Notas:
    Soma += nota
    Quantidade += 1 

media = Soma / Quantidade
print(f'Media: {media:.2}')

# 5 Questão

Numeros = [14, 3, 28, 9, 45, 2]

Maior = Numeros[0]
Menor = Numeros[0]

for num in Numeros:
    if num > Maior:
        Maior = num
    if num < Menor: 
        Menor = num

print('Maior', Maior)
print('Menor', Menor)

# 6 Questão

numeros = [12, 5, 8, 19, 22, 7, 30, 11, 4, 15]

pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)

# 7 Questão

Numerosumeros = []
for i in range(8):
    num = int(input(f"Digite o {i+1}º número: "))
    Numerosumeros.append(num)

busca = int(input("Digite um número para buscar: "))

encontrado = False
for num in numeros:
    if num == busca:
        encontrado = True
        break

if encontrado:
    print('O número está na lista.')
else:
    print('O número NÃO está na lista.')

# 8 Questão

nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
busca = input("Digite o nome procurado: ")

posicao = -1
for i in range(len(nomes)):
    if nomes[i] == busca:
        posicao = i
        break

if posicao != -1:
    print(f"Nome encontrado na posição (índice): {posicao}")
else:
    print("Nome não encontrado.")

# 9 Questão

numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("Lista antes da remoção:", numeros)

remover = int(input("Digite um número para remover: "))

if remover in numeros:
    numeros.remove(remover)
    print("Lista após a remoção:", numeros)
else:
    print("Número não encontrado na lista. A lista permanece:", numeros)

# 10 Questão

numeros = [18, 5, 12, 3, 20, 7, 9]

print("Original:", numeros)

crescente = sorted(numeros)
print("Crescente (sorted):", crescente)

numeros.sort(reverse=True)
print("Decrescente (sort):", numeros)

# 11 Questão

valores = [10, 20, 30, 40, 50, 60, 70, 80]

print("Quatro primeiros:", valores[:4])
print("Três últimos:", valores[-3:])
print("Posições 2 a 5:", valores[2:6])
print("Lista invertida:", valores[::-1])

# 12 Questão

numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
sem_repeticao = []

for num in numeros:
    if num not in sem_repeticao:
        sem_repeticao.append(num)

print("Lista original:", numeros)
print("Sem repetição:", sem_repeticao)

# 13 Questão

numeros = []
for i in range(10):
    val = float(input(f"Digite o {i+1}º número real: "))
    numeros.append(val)

soma = 0
for val in numeros:
    soma += val

media = soma / len(numeros)
print(f"\nMédia dos valores: {media:.2f}")

print("Valores acima da média:")
for val in numeros:
    if val > media:
        print(val)

# 14 Questão 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrados = [x**2 for x in numeros]
pares = [x for x in numeros if x % 2 == 0]
maiores_que_5 = [x for x in numeros if x > 5]

print("Quadrados:", quadrados)
print("Pares:", pares)
print("Maiores que 5:", maiores_que_5)

# 15 Questão 

alunos = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
notas = [7.5, 4.0, 6.0, 8.5, 5.5]

for i in range(len(alunos)):
    situacao = "Aprovado(a)" if notas[i] >= 6.0 else "Reprovado(a)"
    print(f"Aluno: {alunos[i]} | Nota: {notas[i]} | Situação: {situacao}")

# 16 Questão

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total = 0

print("Elementos da matriz:")
for i in range(len(matriz)):
    soma_linha = 0
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
        soma_linha += matriz[i][j]
        soma_total += matriz[i][j]
    print(f"-> Soma da linha {i+1}: {soma_linha}")

print("\nSoma de todos os valores:", soma_total)

# 17 Questão

numeros = [12, 35, 1, 10, 34, 35, 2]

maior = float('-inf')
segundo_maior = float('-inf')

for num in numeros:
    if num > maior:
        segundo_maior = maior
        maior = num
    elif num > segundo_maior and num != maior:
        segundo_maior = num

print("Maior:", maior)
print("Segundo maior distinto:", segundo_maior)

# 18 Questão

numeros = [2, 3, 2, 5, 3, 2]
contados = []

for num in numeros:
    if num not in contados:
        qtd = 0
        for x in numeros:
            if x == num:
                qtd += 1
        print(f"O valor {num} aparece {qtd} vez(es).")
        contados.append(num)

# 19 Questão

Produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
Quantidades = [12, 25, 4, 3, 8]

Consulta = input("Digite o nome do produto para consultar: ")
Encontrado = False
for i in range(len(Produtos)):
    if Produtos[i].lower() == Consulta.lower():
        print(f"Produto: {Produtos[i]} | Quantidade em estoque: {Quantidades[i]}")
        Encontrado = True
        break
if not Encontrado:
    print("Produto não cadastrado.")

prod_alterar = input("\nDigite o produto para alterar o estoque: ")
for i in range(len(Produtos)):
    if Produtos[i].lower() == prod_alterar.lower():
        nova_quantidade = int(input(f"Digite a nova quantidade para {Produtos[i]}: "))
        Quantidades[i] = nova_quantidade
        print("Quantidade atualizada!")
        break

print("\nProdutos com estoque inferior a 5 unidades:")
for i in range(len(Produtos)):
    if Quantidades[i] < 5:
        print(f"- {Produtos[i]}: {Quantidades[i]} unidades")

maior_quantidade = Quantidades[0]
produção_maior = Produtos[0]

for i in range(1, len(Produtos)):
    if Quantidades[i] > maior_quantidade:
        maior_quantidade = Quantidades[i]
        produção_maior = Produtos[i]

print(f"\nProduto com maior estoque: {produção_maior} ({maior_quantidade} unidades)")

# 20 Questão

vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]

Total_Vendido = 0
for v in vendas:
    Total_Vendido += v

dias = len(vendas)
Media_Diaria = Total_Vendido / dias

Maior_Venda = vendas[0]
Menor_Venda = vendas[0]

for v in vendas:
    if v > Maior_Venda:
        Maior_Venda = v
    if v < Menor_Venda:
        Menor_Venda = v

Acima_da_Média = 0
for v in vendas:
    if v > Media_Diaria:
        Acima_da_Média += 1

Percentual_Acima = (Acima_da_Média / dias) * 100

print(f"Total vendido: R$ {Total_Vendido:.2f}")
print(f"Média diária: R$ {Media_Diaria:.2f}")
print(f"Maior venda: R$ {Maior_Venda:.2f}")
print(f"Menor venda: R$ {Menor_Venda:.2f}")
print(f"Dias acima da média: {Acima_da_Média} dia(s)")
print(f"Percentual de dias acima da média: {Percentual_Acima:.2f}%")