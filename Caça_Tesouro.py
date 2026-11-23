import random

def jogo_caca_ao_tesouro():
    # Cria uma matriz 5x5 preenchida com '~' representando o mapa desconhecido
    tamanho = 5
    mapa = [["~" for _ in range(tamanho)] for _ in range(tamanho)]

    # Define a posição aleatória do tesouro (índices de 0 a 4)
    tesouro_linha = random.randint(0, tamanho - 1)
    tesouro_coluna = random.randint(0, tamanho - 1)

    tentativas = 0
    encontrou = False

    print("=== CAÇA AO TESOURO (5x5) ===")
    print("Tente encontrar o tesouro! Informe linha e coluna de 0 a 4.\n")

    while not encontrou:
        # Exibe o mapa atual
        print("   0 1 2 3 4")
        for i in range(tamanho):
            print(f"{i}  " + " ".join(mapa[i]))
        print()

        # Entrada e validação do usuário
        try:
            linha = int(input("Digite a linha (0 a 4): "))
            coluna = int(input("Digite a coluna (0 a 4): "))

            if not (0 <= linha < tamanho and 0 <= coluna < tamanho):
                print("Posição inválida! Digite valores entre 0 e 4.\n")
                continue
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.\n")
            continue

        tentativas += 1

        # Verifica se acertou o tesouro
        if linha == tesouro_linha and coluna == tesouro_coluna:
            mapa[linha][coluna] = "T"
            encontrou = True
            print("\n   0 1 2 3 4")
            for i in range(tamanho):
                print(f"{i}  " + " ".join(mapa[i]))
            print(
                f"\nPARABÉNS! Você encontrou o tesouro na posição ({linha}, {coluna})!"
            )
            print(f"Total de tentativas: {tentativas}")
        else:
            # Marca a tentativa no mapa
            mapa[linha][coluna] = "X"

            # Calcula a distância de Manhattan até o tesouro
            distancia = abs(linha - tesouro_linha) + abs(
                coluna - tesouro_coluna
            )

            if distancia == 1:
                print("Dica: Muito perto!\n")
            elif distancia in (2, 3):
                print("Dica: Perto!\n")
            else:
                print("Dica: Longe!\n")


if __name__ == "__main__":
    jogo_caca_ao_tesouro()