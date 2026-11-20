from pathlib import Path
import random
import time


def heapify(lista, tamanho, indice):
  while True:
    maior = indice
    esquerda = 2 * indice + 1
    direita = 2 * indice + 2

    if esquerda < tamanho and lista[esquerda] > lista[maior]:
      maior = esquerda

    if direita < tamanho and lista[direita] > lista[maior]:
      maior = direita

    if maior == indice:
      break

    lista[indice], lista[maior] = lista[maior], lista[indice]
    indice = maior


def heap_sort(lista):
  tamanho = len(lista)

  for i in range(tamanho // 2 - 1, -1, -1):
    heapify(lista, tamanho, i)

  for fim in range(tamanho - 1, 0, -1):
    lista[0], lista[fim] = lista[fim], lista[0]
    heapify(lista, fim, 0)

  return lista


def resolver_caminho_arquivo(caminho):
  if not caminho.exists():
    return caminho

  while True:
    print(f"\nO arquivo '{caminho.name}' já existe.")
    print("1 - Sobrescrever arquivo existente")
    print("2 - Salvar com outro nome (ex: *_novo.txt)")
    print("3 - Cancelar operação")
    opcao = input("Escolha uma opção (1/2/3): ").strip()

    if opcao == "1":
      return caminho
    elif opcao == "2":
      novo_caminho = caminho.with_name(f"{caminho.stem}_novo{caminho.suffix}")
      contador = 1
      while novo_caminho.exists():
        novo_caminho = caminho.with_name(
            f"{caminho.stem}_novo_{contador}{caminho.suffix}"
        )
        contador += 1
      return novo_caminho
    elif opcao == "3":
      return None
    else:
      print("Opção inválida. Digite 1, 2 ou 3.")


def gerar_arquivo_entrada(caminho_padrao, quantidade=100_000, minimo=0, maximo=1_000_000):
  caminho_final = resolver_caminho_arquivo(caminho_padrao)
  if caminho_final is None:
    print("Geração do arquivo de entrada cancelada.")
    return None

  try:
    with caminho_final.open("w", encoding="utf-8") as arquivo:
      for _ in range(quantidade):
        numero = random.randint(minimo, maximo)
        arquivo.write(f"{numero}\n")
    print(f"Arquivo '{caminho_final.name}' criado com {quantidade} números.")
    return caminho_final
  except OSError as erro:
    print(f"Erro ao criar o arquivo '{caminho_final.name}': {erro}")
    return None


def ler_numeros_do_arquivo(caminho):
  if caminho is None or not caminho.exists():
    print("Arquivo de entrada não encontrado para leitura.")
    return None

  numeros = []
  linhas_ignoradas = 0

  try:
    with caminho.open("r", encoding="utf-8") as arquivo:
      for numero_linha, linha in enumerate(arquivo, start=1):
        texto = linha.strip()
        if not texto:
          continue
        try:
          numeros.append(int(texto))
        except ValueError:
          linhas_ignoradas += 1
          print(f"Aviso: linha {numero_linha} inválida ('{texto}') ignorada.")

    if linhas_ignoradas > 0:
      print(f"Total de linhas inválidas ignoradas: {linhas_ignoradas}")

    return numeros
  except OSError as erro:
    print(f"Erro ao ler o arquivo '{caminho.name}': {erro}")
    return None


def salvar_arquivo_ordenado(caminho_padrao, numeros):
  caminho_final = resolver_caminho_arquivo(caminho_padrao)
  if caminho_final is None:
    print("Salvamento do arquivo ordenado cancelado.")
    return None

  try:
    with caminho_final.open("w", encoding="utf-8") as arquivo:
      for numero in numeros:
        arquivo.write(f"{numero}\n")
    print(f"Arquivo ordenado salvo em '{caminho_final.name}'.")
    return caminho_final
  except OSError as erro:
    print(f"Erro ao salvar o arquivo '{caminho_final.name}': {erro}")
    return None


def main():
  pasta_script = Path(__file__).resolve().parent
  entrada_padrao = pasta_script / "numeros_aleatorios.txt"
  saida_padrao = pasta_script / "numeros_ordenados.txt"

  arquivo_entrada = gerar_arquivo_entrada(entrada_padrao, quantidade=100_000)
  if arquivo_entrada is None:
    return

  numeros = ler_numeros_do_arquivo(arquivo_entrada)
  if not numeros:
    print("Nenhum número válido encontrado para ordenar.")
    return

  inicio = time.perf_counter()
  heap_sort(numeros)
  fim = time.perf_counter()

  arquivo_saida = salvar_arquivo_ordenado(saida_padrao, numeros)
  if arquivo_saida is None:
    return

  print("\n--- Resumo da execução ---")
  print(f"Elementos ordenados: {len(numeros)}")
  print(f"Tempo do Heap Sort: {fim - inicio:.5f} segundos")
  print(f"Primeiros 10 números: {numeros[:10]}")
  print(f"Últimos 10 números: {numeros[-10:]}")


if __name__ == "__main__":
  main()
