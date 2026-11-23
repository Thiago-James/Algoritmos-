def simulacao_cavalo():
    tamanho = 8
    tabuleiro = [["." for _ in range(tamanho)] for _ in range(tamanho)]

    print("SIMULAÇÃO DE MOVIMENTOS DO CAVALO (8x8)")

    while True:
        try:
            linha = int(input("Informe a linha inicial do cavalo (0 a 7): "))
            coluna = int(input("Informe a coluna inicial do cavalo (0 a 7): "))

            if 0 <= linha < tamanho and 0 <= coluna < tamanho:
                break
            else:
                print(
                    "Posição fora do tabuleiro! Digite valores entre 0 e 7.\n"
                )
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.\n")

    tabuleiro[linha][coluna] = "C"

    movimentos_possiveis = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]

    for dl, dc in movimentos_possiveis:
        nova_linha = linha + dl
        nova_coluna = coluna + dc

        if 0 <= nova_linha < tamanho and 0 <= nova_coluna < tamanho:
            tabuleiro[nova_linha][nova_coluna] = "*"

    print("\nTabuleiro final (C = Cavalo | * = Movimento válido | . = Vazio):")
    print("   0 1 2 3 4 5 6 7")
    for i in range(tamanho):
        print(f"{i}  " + " ".join(tabuleiro[i]))


if __name__ == "__main__":
    simulacao_cavalo()