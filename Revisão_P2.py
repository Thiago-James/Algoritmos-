def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas) if notas else 0


def contar_aprovados(notas):
    aprovados = 0
    for nota in notas:
        if nota >= 6:
            aprovados += 1
    return aprovados


def obter_maior_e_menor(notas):
    maior = notas[0]
    menor = notas[0]
    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
    return maior, menor


def main():
    notas = []
    quantidade_alunos = 10

    for i in range(quantidade_alunos):
        while True:
            nota = float(input(f"Digite a nota do {i + 1}º aluno (0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            print("Nota inválida! Digite um valor entre 0 e 10.")

    media = calcular_media(notas)
    aprovados = contar_aprovados(notas)
    reprovados = len(notas) - aprovados
    maior_nota, menor_nota = obter_maior_e_menor(notas)

    print("\n--- Resumo da Turma ---")
    print(f"Média da turma: {media:.2f}")
    print(f"Aprovados (>= 6): {aprovados}")
    print(f"Reprovados (< 6): {reprovados}")
    print(f"Maior nota: {maior_nota:.2f}")
    print(f"Menor nota: {menor_nota:.2f}")


if __name__ == "__main__":
    main()

# Q2

def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        for j in range(0, n - 1 - i):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1

    return arr, comparacoes, trocas


def main():
    precos = [49.90, 19.50, 129.00, 15.00, 89.90, 34.50, 210.00, 9.99]

    print("Preços antes da ordenação:", precos)
    precos_ordenados, comparacoes, trocas = bubble_sort(precos)
    print("Preços ordenados (crescente):", precos_ordenados)
    print(f"Total de comparações: {comparacoes}")
    print(f"Total de trocas: {trocas}")


if __name__ == "__main__":
    main()

# Q3

def calcular_faturamento(pedidos):
    total = 0.0
    for valor in pedidos:
        total += valor
    return total


def identificar_maior_pedido(pedidos):
    if not pedidos:
        return 0.0
    maior = pedidos[0]
    for valor in pedidos:
        if valor > maior:
            maior = valor
    return maior


def calcular_media_pedidos(pedidos):
    if not pedidos:
        return 0.0
    return calcular_faturamento(pedidos) / len(pedidos)


def main():
    pedidos = []

    while True:
        valor = float(input("Digite o valor do pedido (0 para encerrar): "))
        if valor == 0:
            break
        if valor < 0:
            print("Valor inválido! Digite um valor positivo ou 0 para encerrar.")
            continue
        pedidos.append(valor)

    quantidade = len(pedidos)
    faturamento = calcular_faturamento(pedidos)
    maior_pedido = identificar_maior_pedido(pedidos)
    media_pedido = calcular_media_pedidos(pedidos)

    print("\n--- Relatório do Dia ---")
    print(f"Quantidade de pedidos: {quantidade}")
    print(f"Faturamento total: R$ {faturamento:.2f}")
    print(f"Maior pedido: R$ {maior_pedido:.2f}")
    print(f"Média dos pedidos: R$ {media_pedido:.2f}")


if __name__ == "__main__":
    main()

# Q4

def soma_total_estoque(quantidades):
    total = 0
    for qtd in quantidades:
        total += qtd
    return total


def contar_unidades_zeradas(quantidades):
    zeradas = 0
    for qtd in quantidades:
        if qtd == 0:
            zeradas += 1
    return zeradas


def existe_quantidade_exata(quantidades, quantidade_desejada):
    for qtd in quantidades:
        if qtd == quantidade_desejada:
            return True
    return False


def main():
    estoque = [12, 0, 25, 8, 0, 15]  # 6 unidades

    total = soma_total_estoque(estoque)
    zeradas = contar_unidades_zeradas(estoque)

    print("Estoque por unidade:", estoque)
    print(f"Soma total de itens: {total}")
    print(f"Unidades com estoque zero: {zeradas}")

    busca = int(input("Informe uma quantidade desejada para verificar se existe em alguma unidade: "))
    if existe_quantidade_exata(estoque, busca):
        print(f"Sim, existe pelo menos uma unidade com exatamente {busca} itens.")
    else:
        print(f"Não, nenhuma unidade possui exatamente {busca} itens.")


if __name__ == "__main__":
    main()

# Q5

def soma_iterativa(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def soma_recursiva(n):
    # Caso-base
    if n <= 0:
        return 0
    # Chamada recursiva
    return n + soma_recursiva(n - 1)


def main():
    testes = [5, 10, 100]

    for n in testes:
        res_iter = soma_iterativa(n)
        res_rec = soma_recursiva(n)
        print(f"N = {n:3d} -> Iterativa: {res_iter:4d} | Recursiva: {res_rec:4d}")


if __name__ == "__main__":
    main()


# Q7

def calcular_media(pontuacoes):
    if not pontuacoes:
        return 0.0
    return soma_recursiva(pontuacoes) / len(pontuacoes)


def maior_pontuacao(pontuacoes):
    if not pontuacoes:
        return None
    maior = pontuacoes[0]
    for pontos in pontuacoes:
        if pontos > maior:
            maior = pontos
    return maior


def bubble_sort_decrescente(pontuacoes):
    ranking = pontuacoes.copy()
    n = len(ranking)

    for i in range(n):
        for j in range(0, n - 1 - i):
            if ranking[j] < ranking[j + 1]:
                ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

    return ranking


def soma_recursiva(pontuacoes):
    if len(pontuacoes) == 0:
        return 0
    return pontuacoes[0] + soma_recursiva(pontuacoes[1:])


def exibir_ranking(ranking):
    print("\n--- Ranking (Ordem Decrescente) ---")
    for posicao, pontos in enumerate(ranking, start=1):
        print(f"{posicao}º lugar: {pontos}")


def main():
    pontuacoes = []

    while True:
        entrada = float(input("Digite a pontuação do participante (-1 para encerrar): "))
        if entrada == -1:
            break
        if entrada < 0:
            print("Pontuação inválida! Digite um valor >= 0 ou -1 para encerrar.")
            continue
        pontuacoes.append(entrada)

    total_participantes = len(pontuacoes)
    media = calcular_media(pontuacoes)
    maior = maior_pontuacao(pontuacoes)
    ranking = bubble_sort_decrescente(pontuacoes)

    print("\n=== Resumo da Competição ===")
    print(f"Quantidade de participantes: {total_participantes}")
    print(f"Média das pontuações: {media:.2f}")
    print(f"Maior pontuação: {maior if maior is not None else 0}")
    exibir_ranking(ranking)


if __name__ == "__main__":
    main()
