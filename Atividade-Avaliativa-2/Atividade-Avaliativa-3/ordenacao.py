# Situação-problema: Central de Distribuição de Pedidos
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

# Insertion Sort

def insertion_sort(vetor):

    comparacoes = 0
    movimentacoes = 0

    # Começa no índice 1

    for i in range(1, len(vetor)):

        key = vetor[i]
        j = i - 1

        # Ordena da esquerda para direita

        while j >= 0:

            # Conta uma comparação

            comparacoes += 1

            if vetor[j] > key:

                # Move o elemento para a direita

                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1

            else:
                break

        # Coloca o elemento na posição correta

        vetor[j + 1] = key
        movimentacoes += 1

    return comparacoes, movimentacoes

# Selection Sort

def selection_sort(vetor):

    comparacoes = 0
    trocas = 0
    n = len(vetor)

    for i in range(n - 1):

        # Considera o primeiro elemento como o menor

        indice_minimo = i

        # Procura o menor elemento

        for j in range(i + 1, n):

            # Conta uma comparação

            comparacoes += 1

            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j

        # Troca o menor elemento encontrado
        
        if indice_minimo != i:

            vetor[i], vetor[indice_minimo] = (vetor[indice_minimo], vetor[i])

            # Conta uma troca

            trocas += 1

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

        vetor[i + 1], vetor[fim] = (vetor[fim], vetor[i + 1])

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
    vetor_insertion = original.copy()
    vetor_selection = original.copy()
    vetor_quick = original.copy()

    # Bubble Sort

    comparacoes_bubble, trocas_bubble = bubble_sort(vetor_bubble)

    # Insertion Sort

    comparacoes_insertion, movimentacoes_insertion = insertion_sort(vetor_insertion)

    # Selection Sort

    comparacoes_selection, trocas_selection = selection_sort(vetor_selection)

    # Quick Sort

    contador_quick = {"comparacoes": 0, "movimentacoes": 0}

    quick_sort(vetor_quick, 0, len(vetor_quick) - 1, contador_quick)

    # Guarda os resultados

    resultados.append(
        {
            "tamanho": tamanho,
            "bubble_comparacoes": comparacoes_bubble,
            "bubble_trocas": trocas_bubble,
            "insertion_comparacoes": comparacoes_insertion,
            "insertion_movimentacoes": movimentacoes_insertion,
            "selection_comparacoes": comparacoes_selection,
            "selection_trocas": trocas_selection,
            "quick_comparacoes": contador_quick["comparacoes"],
            "quick_movimentacoes": contador_quick["movimentacoes"],
        }
    )

# Mostrar Resultados

print("-" * 160)

print(
    f"{'Tamanho':<12}"
    f"{'Bubble Comp.':<18}"
    f"{'Bubble Trocas':<18}"
    f"{'Insertion Comp.':<20}"
    f"{'Insertion Mov.':<20}"
    f"{'Selection Comp.':<20}"
    f"{'Selection Trocas':<20}"
    f"{'Quick Comp.':<18}"
    f"{'Quick Mov.':<18}"
)

print("-" * 160)

for resultado in resultados:

    print(
        f"{resultado['tamanho']:<12}"
        f"{resultado['bubble_comparacoes']:<18}"
        f"{resultado['bubble_trocas']:<18}"
        f"{resultado['insertion_comparacoes']:<20}"
        f"{resultado['insertion_movimentacoes']:<20}"
        f"{resultado['selection_comparacoes']:<20}"
        f"{resultado['selection_trocas']:<20}"
        f"{resultado['quick_comparacoes']:<18}"
        f"{resultado['quick_movimentacoes']:<18}"
    )

print("-" * 160)

