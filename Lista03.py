# Aluno: Thiago

# N1

Numeros = [12, 45, 7, 23, 56, 34, 90, 11, 67]
Foco = int(input('Digite um número inteiro: '))
encontrado = False

for item in Numeros:
    if item == Foco:
        encontrado = True 
        break

if encontrado:
    print(f'O número {Foco} está na lista.')
else:
    print(f'O número {Foco} não está na lista.')

# N2

Nomes = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduarda']
Foco = input('Digite nome: ')
posição = -1

for i in range(len(Nomes)):
    if Nomes[i] == Foco:
        posição = i
        break

if posição != -1:
    print(f'O nome {Foco} está na lista na posição {posição}.')
else:
    print(f'O nome {Foco} não está na lista.')

# N3

def buscar_numero(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i 
    return -1

# N4

notas = [7.5, 6.5, 7.7, 9.9, 10.0, 2.2]
Foco = float(input('Digite a nota procurada: '))
contador = 0

for nota in notas:
    if nota == Foco:
        contador += 1

if contador > 0:
    print(f'A nota {Foco} aparece {contador} vezes na lista.')
else:
    print(f'A nota {Foco} não aparece na lista.')

# N5

produtos = ['Carne', 'Macarrão', 'Leite', 'Manteiga', 'Ovos']
Foco = input('Digite o nome do produto:')
Posição = -1

for i in range(len(produtos)):
    if produtos[i].lower() == Foco.lower():
        Posição = i 
        break

 if posição != -1:
    print(f'O produto {produtos[posição]} custa R$ {preços[posição]:.2f}.')
else:
    print('Produto não localizado.')

# N6

Numeros = [23, 89, 12, 45, 99, 34, 67]
Maior = Numeros[0]

for i in range(1, len(Numeros)):
    if Numeros[i] > Maior:
        Maior = Numeros[i]

print(f'O maior número na lista é: {Maior}')

# N7

import random

Numeros = [random.randint(1, 10) for _ in range(15)]
print('Lista:', Numeros)
Foco = int(input('Digite um valor: '))
posições = []

for i in range(len(Numeros)):
    if Numeros[i] == Foco:
        posições.append(i)

if posições:
    print(f'O valor {Foco} aparece nas oposições: {posições}')
else:
    print(f'O valor {Foco} não foi encontrado. ')

# N8

def existe_na_lista(lista, numero):
    for item in lista:
        if item == numero:
            return True
        return False

# N9

matriculas = [20260187, 20261214, 20260131, 20260135, 20260127]
alvo = int(input("Digite a matrícula do aluno: "))
cadastrado = False

for m in matriculas:
    if m == alvo:
        cadastrado = True
        break

if cadastrado:
    print("Aluno cadastrado!")
else:
    print("Matrícula não encontrada.")

# N10

palavras = ["Python", "Algoritmos", "Estrutura", "Desenvolvimento", "Lista"]
maior_palavra = palavras[0]

for i in range(1, len(palavras)):
    if len(palavras[i]) > len(maior_palavra):
        maior_palavra = palavras[i]

print(f"A palavra mais longa é '{maior_palavra}' com {len(maior_palavra)} caracteres.")

# N11

cpfs = ["111.222.333-44", "222.333.444-55", "333.444.555-66", "444.555.666-77"]
alvo = input("Digite o CPF (com pontos e hífen): ")
comparacoes = 0
encontrado = False

for cpf in cpfs:
    comparacoes += 1
    if cpf == alvo:
        encontrado = True
        break

if encontrado:
    print(f"CPF cadastrado! Comparações realizadas: {comparacoes}")
else:
    print(f"CPF não encontrado. Comparações realizadas: {comparacoes}")


# N12

numeros = [10, 25, 30, 45, 50, 65, 70]
alvo = int(input("Valor a buscar: "))
comparacoes = 0
posicao = -1

for i in range(len(numeros)):
    comparacoes += 1
    if numeros[i] == alvo:
        posicao = i
        break

if posicao != -1:
    print(f"Valor: {numeros[posicao]} | Posição: {posicao} | Comparações: {comparacoes}")
else:
    print(f"Valor não encontrado após {comparacoes} comparações.")

# N13

lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
alvo = int(input("Digite um número: "))

inicio = 0
fim = len(lista) - 1
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        posicao = meio
        break
    elif lista[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

if posicao != -1:
    print(f"Número encontrado no índice {posicao}.")
else:
    print("Número não encontrado.")

# N14

def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# N15

nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernanda", "Gabriel"]
alvo = input("Digite o nome: ")

inicio = 0
fim = len(nomes) - 1
encontrado = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    if nomes[meio].lower() == alvo.lower():
        encontrado = True
        break
    elif nomes[meio].lower() < alvo.lower():
        inicio = meio + 1
    else:
        fim = meio - 1

print("Nome presente na lista!" if encontrado else "Nome não encontrado.")

# N16

numeros = list(range(5, 105, 5))  # 20 números
alvo = int(input("Digite um número para buscar: "))

inicio = 0
fim = len(numeros) - 1
passo = 1

while inicio <= fim:
    meio = (inicio + fim) // 2
    print(f"Iteração {passo}: inicio={inicio}, fim={fim}, meio={meio} (valor={numeros[meio]})")
    passo += 1
    
    if numeros[meio] == alvo:
        print("Encontrado!")
        break
    elif numeros[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

# N17

codigos = [101, 105, 202, 304, 400, 501, 608]
alvo = int(input("Digite o código do produto: "))

inicio = 0
fim = len(codigos) - 1
achou = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    if codigos[meio] == alvo:
        achou = True
        break
    elif codigos[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

print("Código cadastrado!" if achou else "Código inexistente.")

# N18

def busca_binaria_compara(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0
    
    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio, comparacoes
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

# N19

def busca_binaria_bool(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return True
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return False

# N20

pares = list(range(2, 201, 2))
alvo = int(input("Digite um número par: "))

inicio = 0
fim = len(pares) - 1
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if pares[meio] == alvo:
        posicao = meio
        break
    elif pares[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

if posicao != -1:
    print(f"O número {alvo} foi localizado no índice {posicao}.")
else:
    print("Número não encontrado.")

# N21

lista = [1, 3, 5, 5, 5, 8, 10, 12]
alvo = 5

inicio = 0
fim = len(lista) - 1
pos = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        pos = meio
        break  # Retorna qualquer uma das ocorrências
    elif lista[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

print(f"Uma ocorrência de {alvo} está no índice {pos}.")

# N22

def primeira_ocorrencia(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            resultado = meio
            fim = meio - 1  # Continua buscando na metade esquerda
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resultado

# N23

def ultima_ocorrencia(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            resultado = meio
            inicio = meio + 1  # Continua buscando na metade direita
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resultado

# N24

idades = [12, 15, 18, 20, 22, 25, 30, 35, 40, 45, 50, 60]
alvo = int(input("Digite a idade: "))

inicio = 0
fim = len(idades) - 1
descartados = 0
encontrado = False

while inicio <= fim:
    meio = (inicio + fim) // 2
    if idades[meio] == alvo:
        encontrado = True
        break
    elif idades[meio] < alvo:
        descartados += (meio - inicio + 1)
        inicio = meio + 1
    else:
        descartados += (fim - meio + 1)
        fim = meio - 1

if encontrado:
    print(f"Idade encontrada! Total de elementos descartados: {descartados}")
else:
    print(f"Idade não encontrada. Elementos descartados: {len(idades)}")

# N25

codigos_livros = [1001, 1005, 1012, 1020, 1035, 1050, 1088]
alvo = int(input("Digite o código do livro: "))

inicio = 0
fim = len(codigos_livros) - 1
pos = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if codigos_livros[meio] == alvo:
        pos = meio
        break
    elif codigos_livros[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

if pos != -1:
    print(f"Livro disponível! Localizado no índice {pos}.")
else:
    print("Livro indisponível na biblioteca.")

# N26
produtos = [101, 104, 109, 115, 120, 130, 142]
alvo = 130

comp_seq = 0
for p in produtos:
    comp_seq += 1
    if p == alvo:
        break

comp_bin = 0
inicio, fim = 0, len(produtos) - 1
while inicio <= fim:
    comp_bin += 1
    meio = (inicio + fim) // 2
    if produtos[meio] == alvo:
        break
    elif produtos[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

print(f"Busca Sequencial precisou de {comp_seq} comparações.")
print(f"Busca Binária precisou de {comp_bin} comparações.")

# N27

matriculas = [202, 101, 505, 303, 404]

opcao = int(input("Escolha o método de busca: (1) Sequencial (2) Binária: "))
alvo = int(input("Digite a matrícula: "))

if opcao == 1:
    encontrado = False
    for m in matriculas:
        if m == alvo:
            encontrado = True
            break
    print("Encontrado!" if encontrado else "Não encontrado.")

elif opcao == 2:
    lista_ord = matriculas.copy()
    for i in range(len(lista_ord)):
        for j in range(0, len(lista_ord) - i - 1):
            if lista_ord[j] > lista_ord[j+1]:
                lista_ord[j], lista_ord[j+1] = lista_ord[j+1], lista_ord[j]
    
    inicio, fim = 0, len(lista_ord) - 1
    encontrado = False
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ord[meio] == alvo:
            encontrado = True
            break
        elif lista_ord[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    print("Encontrado!" if encontrado else "Não encontrado.")

# N28

dados = list(range(1, 1001))
alvo = 1000

comp_seq = 0
for x in dados:
    comp_seq += 1
    if x == alvo:
        break

comp_bin = 0
inicio, fim = 0, len(dados) - 1
while inicio <= fim:
    comp_bin += 1
    meio = (inicio + fim) // 2
    if dados[meio] == alvo:
        break
    elif dados[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1

print(f"Busca Sequencial: {comp_seq} comparações.")
print(f"Busca Binária: {comp_bin} comparações.")
print("Conclusão: A busca binária é absurdamente mais eficiente em listas grandes e ordenadas (O(log n) vs O(n)).")

agenda = [
    {"nome": "Ana", "telefone": "9999-1111"},
    {"nome": "Bruno", "telefone": "9999-2222"},
    {"nome": "Carla", "telefone": "9999-3333"},
    {"nome": "Daniel", "telefone": "9999-4444"}
]

alvo = input("Nome a buscar: ")
inicio, fim = 0, len(agenda) - 1
pos = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if agenda[meio]["nome"].lower() == alvo.lower():
        pos = meio
        break
    elif agenda[meio]["nome"].lower() < alvo.lower():
        inicio = meio + 1
    else:
        fim = meio - 1

if pos != -1:
    print(f"Contato: {agenda[pos]['nome']} | Telefone: {agenda[pos]['telefone']}")
else:
    print("Contato não encontrado.")

# N29

agenda = [
    {"nome": "Ana", "telefone": "9999-1111"},
    {"nome": "Bruno", "telefone": "9999-2222"},
    {"nome": "Carla", "telefone": "9999-3333"},
    {"nome": "Daniel", "telefone": "9999-4444"}
]

alvo = input("Nome a buscar: ")
inicio, fim = 0, len(agenda) - 1
pos = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    if agenda[meio]["nome"].lower() == alvo.lower():
        pos = meio
        break
    elif agenda[meio]["nome"].lower() < alvo.lower():
        inicio = meio + 1
    else:
        fim = meio - 1

if pos != -1:
    print(f"Contato: {agenda[pos]['nome']} | Telefone: {agenda[pos]['telefone']}")
else:
    print("Contato não encontrado.")

# N30

lista = []
ordenada = False

while True:
    print("\n--- MENU ---")
    print("1. Cadastrar valores")
    print("2. Exibir lista")
    print("3. Ordenar lista")
    print("4. Realizar busca sequencial")
    print("5. Realizar busca binária")
    print("0. Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        val = int(input("Digite um valor inteiro: "))
        lista.append(val)
        ordenada = False
    elif opcao == "2":
        print("Lista:", lista)
    elif opcao == "3":
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        ordenada = True
        print("Lista ordenada com sucesso!")
    elif opcao == "4":
        alvo = int(input("Valor a buscar: "))
        achou = False
        for i in range(len(lista)):
            if lista[i] == alvo:
                print(f"Encontrado no índice {i}.")
                achou = True
                break
        if not achou:
            print("Não encontrado.")
    elif opcao == "5":
        if not ordenada:
            print("Erro: A busca binária exige que a lista esteja ordenada (Opção 3).")
        else:
            alvo = int(input("Valor a buscar: "))
            inicio, fim = 0, len(lista) - 1
            achou = False
            while inicio <= fim:
                meio = (inicio + fim) // 2
                if lista[meio] == alvo:
                    print(f"Encontrado no índice {meio}.")
                    achou = True
                    break
                elif lista[meio] < alvo:
                    inicio = meio + 1
                else:
                    fim = meio - 1
            if not achou:
                print("Não encontrado.")
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")