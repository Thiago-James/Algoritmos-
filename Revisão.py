# Tarefa 1 - Cálculo do Volume de uma Esfera

import math

raio = float(input("Insira o raio da esfera: "))

volume = (4/3) * math.pi * (raio ** 3)

print(f"O volume da esfera é: {volume: .2f}")

# Tarefa 2 - Classificação de Motoristas com Base em Multas

leves = int(input("O motorista teve multas leves? se sim, quantas? (insira 0 se não houver nenhuma): "))
graves = int(input("O motorista teve multas graves? se sim, quantas? (insira 0 se não houver nenhuma): "))
graviss = int(input("O motorista teve multas gravíssimas? se sim, quantas? (insira 0 se não houver nenhuma): "))

if leves == 0 and graves == 0 and graviss == 0:
    print("O motorista é excelente.")
elif leves <= 2 and graves == 0 and graviss == 0:
    print("O motorista é bom.")
elif (leves <= 4 or graves <= 1) and graviss == 0:
    print("O motorista é regular.")
elif (leves > 4 or graves <= 2) and graviss == 0:
    print("O motorista é ruim.")
elif graves > 2 or graviss >= 1:
    print("O motorista é péssimo")

# Tarefa 3 - Gerenciador de Tarefas Simples


tarefas = []

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nova_tarefa = input("Insira uma nova tarefa: ")
        tarefas.append(nova_tarefa)
        print("Tarefa adicionada.")

    elif opcao == 2:
        if tarefas == []:
            print("Não há tarefas pendentes.")
        else:
            print("Tarefas pendentes:")
            for i, t in enumerate(tarefas):
                print(f"{i} - {t}")

    elif opcao == 3:
        print("Tarefas pendentes:")
        for i, t in enumerate(tarefas):
            print(f"{i} - {t}")
        indice = int(input("Digite o número da tarefa concluída: "))
        tarefas.pop(indice)
        print("Tarefa marcada como concluída.")

    elif opcao == 4:
        break

    else:
        print("Opção inválida.")

# Tarefa 4 - Cálculo Simples de Impostos


tipo_de_bem = int(input("Qual o tipo do seu produto? (Insira 1 para mercadoria e 2 para serviço): "))
valor = float(input("Qual o valor do seu produto?: "))
imposto_imcs = valor + (valor * 18 / 100)
imposto_iss = valor + (valor * 5 / 100)

if tipo_de_bem == 1:
    print(f"O valor do seu produto mais impostos é de:{imposto_imcs: .2f}")
elif tipo_de_bem == 2:
    print(f"O valor do seu produto mais impostos é de:{imposto_iss: .2f}")
else:
    print("Opção inválida.")

# Tarefa 5 - Cálculo de Impostos sobre Salários


salario_bruto = float(input("Qual o salário deste funcionário?: "))

if salario_bruto <= 1500:
    inss = 7.5
elif salario_bruto <= 3000:
    inss = 9
else:
    inss = 12

if salario_bruto <= 2000:
    irpf = 0
elif salario_bruto <= 4000:
    irpf = 7.5
else:
    irpf = 15

salario_liquido = salario_bruto - (salario_bruto * inss / 100) - (salario_bruto * irpf / 100)
print(f"O salário líquido desse funcionário é de:{salario_liquido: .2f}")

# Tarefa 6 - Sistema de Cadastro de Alunos

alunos = []
notas =[]

while True:
    print("\n1 - Adicionar aluno")
    print("2 - Exibir todos os alunos cadastrados")
    print("3 - Calcular a média de um aluno")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
            novo_aluno = input("Cadastre o aluno: ")
            nota_do_aluno = float(input("Insira a nota do aluno: "))
            alunos.append(novo_aluno)
            notas.append(nota_do_aluno)
            print("Aluno cadastrado.")
            
    elif opcao == 2:
            if alunos == []:
                print("Não há alunos cadastrados.")
            else:
                print("Alunos cadastrados:")
                for i, a in enumerate(alunos):
                    print(f"{i} - {a}: nota {notas[i]}")

    elif opcao == 3:
        if alunos == []:
            print("Não há alunos cadastrados.")
        else:
            print("Alunos cadastrados:")
            for i, a in enumerate(alunos):
                print(f"{i} - {a}")
            indice = int(input("Digite o número do aluno: "))
            media = notas[indice]
            if media >= 7:
                print(f"{alunos[indice]} está aprovado com média {media:.2f}.")
            else:
                print(f"{alunos[indice]} está reprovado com média {media:.2f}.")

    elif opcao == 4:
        break

    else:
        print("Opção inválida")