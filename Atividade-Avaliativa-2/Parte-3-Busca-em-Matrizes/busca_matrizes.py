# PARTE 3 - INVESTIGAÇÃO DE BUSCA EM MATRIZES

# Gerador de Matriz
def criar_matriz(linhas, colunas):

    matriz = []

    numero = 1

    for linha in range(linhas):

        nova_linha = []

        for coluna in range(colunas):

            nova_linha.append(numero)

            numero += 1

        matriz.append(nova_linha)

    return matriz


# Matrizes Pedidas:

# Matriz 2x2
matriz2x2 = criar_matriz(2, 2)

# Matriz 10x10
matriz10x10 = criar_matriz(10, 10)

# Matriz 100x100
matriz100x100 = criar_matriz(100, 100)

# Função de Busca Sequencial
def busca_sequencial(matriz, valor_procurado):

    comparacoes = 0

    for linha in range(len(matriz)):

        for coluna in range(len(matriz[linha])):

            comparacoes += 1

            if matriz[linha][coluna] == valor_procurado:

                return True, linha, coluna, comparacoes

    return False, None, None, comparacoes


# Matrizes para Fazer os Testes
matrizes = [
    ("Matriz 2x2", matriz2x2, 3, 5),
    ("Matriz 10x10", matriz10x10, 99, 101),
    ("Matriz 100x100", matriz100x100, 9999, 10001),
]

# Fazer os Testes nas Matrizes
for nome, matriz, proximo_final, inexistente in matrizes:

    print("-" * 50)

    print(nome)

    print("-" * 50)

    # Escolher Elementos para os Testes
    testes = [
        ("Valor no início", 1),
        ("Valor próximo ao final", proximo_final),
        ("Valor inexistente", inexistente),
    ]

    # Fazer Busca nos Elementos
    for descricao, valor in testes:

        encontrado, linha, coluna, comparacoes = busca_sequencial(matriz, valor)

        # Mostrar Resultados
        print("\nTeste:", descricao)

        print("Valor procurado:", valor)

        print("Valor encontrado:", encontrado)

        print("Linha:", linha)

        print("Coluna:", coluna)

        print("Quantidade de comparações:", comparacoes)

print("\n" + "-" * 50)

print("Testes Finalizados!")

print("-" * 50)

