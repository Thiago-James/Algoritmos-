aluno = {"nome": "Thiago", "idade": 20, "curso": "Tecnologia da Informação"}
print("1. Nome do aluno:", aluno["nome"])

aluno["nota"] = 9.5
del aluno["idade"]  
print("2. Dicionário aluno atualizado:", aluno)

produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}
print("\n3. Lista de Produtos:")
for produto, preco in produtos.items():
    print(f"   - {produto}: R$ {preco:.2f}")

print("\n4. Verificação de chave:")
if "curso" in aluno:
    print("   A chave 'curso' existe no dicionário aluno.")
else:
    print("   A chave 'curso' NÃO existe no dicionário aluno.")

turma = {
    "aluno1": {"nome": "Ana", "nota": 8.5},
    "aluno2": {"nome": "Carlos", "nota": 9.0},
}
print("\n5. Dados da Turma:")
print("   Nome do primeiro aluno:", turma["aluno1"]["nome"])
print("   Nota do segundo aluno:", turma["aluno2"]["nota"])

carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2023}
carro["cor"] = "Prata"
print("\n6a. Carro atualizado:", carro)

notas_alunos = {"Lucas": 7.5, "Mariana": 9.2, "Pedro": 6.8}

print("6c. Nota da Mariana:", notas_alunos["Mariana"])

del notas_alunos["Pedro"]
print("6d. Dicionário de notas após remoção:", notas_alunos)

# 02

estoque_supermercado = {
    "P001": {"nome": "Arroz", "preco": 25.90, "estoque": 100},
    "P002": {"nome": "Feijão", "preco": 8.50, "estoque": 60},
    "P003": {"nome": "Café", "preco": 18.00, "estoque": 45},
}

estoque_supermercado["P001"]["estoque"] -= 15
estoque_supermercado["P003"]["preco"] = 19.50

print("=== ESTOQUE DO SUPERMERCADO ===")
for codigo, info in estoque_supermercado.items():
    print(
        f"[{codigo}] {info['nome']} | Preço: R$ {info['preco']:.2f} | Estoque: {info['estoque']} un."
    )

# 03
agenda = {"Maria": "99999-1234", "João": "98888-5678"}

agenda["Fernanda"] = "97777-4321"

agenda["João"] = "98888-0000"

nome_busca = "Maria"
telefone = agenda.get(nome_busca, "Contato não encontrado.")
print(f"Telefone da {nome_busca}: {telefone}")

agenda.pop("Fernanda", None)

print("\n=== AGENDA TELEFÔNICA ===")
for nome, numero in agenda.items():
    print(f"{nome}: {numero}")