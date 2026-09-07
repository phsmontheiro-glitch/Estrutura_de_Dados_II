# PARTE 2 - EXPERIMENTO DE ORDENAÇÃO

# Comparação experimental de quantidade de operações
import random

# Tamanhos pedidos no trabalho
tamanhos = [10, 20, 1000]

# Lista para guardar os resultados
resultados = []


# Bubble Sort
def bubble_sort(vetor):

    comparacoes = 0
    trocas = 0

    n = len(vetor)

    for i in range(n - 1):

        houve_troca = False

        for j in range(n - 1 - i):

            # Conta uma comparação
            comparacoes += 1

            if vetor[j] > vetor[j + 1]:

                # Troca os elementos
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

                # Conta uma troca
                trocas += 1

                houve_troca = True

        # Se não houve troca, o vetor já está ordenado
        if not houve_troca:

            break

    return comparacoes, trocas


# Quick Sort
def particionar(vetor, inicio, fim, contador):

    # Último elemento será o pivô
    pivo = vetor[fim]

    i = inicio - 1

    # Percorre os elementos
    for j in range(inicio, fim):

        # Conta comparação com o pivô
        contador["comparacoes"] += 1

        if vetor[j] <= pivo:

            i += 1

            # Só troca se forem posições diferentes
            if i != j:

                vetor[i], vetor[j] = vetor[j], vetor[i]

                contador["movimentacoes"] += 1

    # Coloca o pivô na posição correta
    if i + 1 != fim:

        vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]

        contador["movimentacoes"] += 1

    return i + 1


def quick_sort(vetor, inicio, fim, contador):

    if inicio < fim:

        # Encontra a posição correta do pivô
        posicao_pivo = particionar(vetor, inicio, fim, contador)

        # Ordena a parte esquerda
        quick_sort(vetor, inicio, posicao_pivo - 1, contador)

        # Ordena a parte direita
        quick_sort(vetor, posicao_pivo + 1, fim, contador)


# Experimento
for tamanho in tamanhos:

    # Gera o array original
    original = [random.randint(1, 10000) for _ in range(tamanho)]

    # Cria cópias para garantir os mesmos dados
    vetor_bubble = original.copy()

    vetor_quick = original.copy()

    # Bubble Sort
    comparacoes_bubble, trocas_bubble = bubble_sort(vetor_bubble)

    # Quick Sort
    contador_quick = {"comparacoes": 0, "movimentacoes": 0}

    quick_sort(vetor_quick, 0, len(vetor_quick) - 1, contador_quick)

    # Guarda os Resultados
    resultados.append(
        {
            "tamanho": tamanho,
            "bubble_comparacoes": comparacoes_bubble,
            "bubble_trocas": trocas_bubble,
            "quick_comparacoes": contador_quick["comparacoes"],
            "quick_movimentacoes": contador_quick["movimentacoes"],
        }
    )

# Mostrar Resultados
print("-" * 90)

print(
    f"{'Tamanho':<12}"
    f"{'Bubble Comp.':<18}"
    f"{'Bubble Trocas':<18}"
    f"{'Quick Comp.':<18}"
    f"{'Quick Mov.':<18}"
)

print("-" * 90)


for resultado in resultados:

    print(
        f"{resultado['tamanho']:<12}"
        f"{resultado['bubble_comparacoes']:<18}"
        f"{resultado['bubble_trocas']:<18}"
        f"{resultado['quick_comparacoes']:<18}"
        f"{resultado['quick_movimentacoes']:<18}"
    )

print("-" * 90)

