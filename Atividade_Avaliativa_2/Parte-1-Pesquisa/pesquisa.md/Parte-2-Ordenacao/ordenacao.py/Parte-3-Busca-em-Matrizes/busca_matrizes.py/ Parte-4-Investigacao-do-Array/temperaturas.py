# PARTE 4 - HANDS ON 1: INVESTIGAÇÃO DO ARRAY

temperaturas = []

# Receber as 10 Temperaturas
for indice in range(10):

    temperatura = float(input(f"Digite a temperatura {indice + 1}: "))

    temperaturas.append(temperatura)


# Analisar Temperaturas
def analisar_temperaturas(temperaturas):

    soma = 0

    maior = temperaturas[0]

    menor = temperaturas[0]

    indice_maior = 0

    indice_menor = 0

    for indice in range(len(temperaturas)):

        temperatura_atual = temperaturas[indice]

        soma += temperatura_atual

        if temperatura_atual > maior:

            maior = temperatura_atual

            indice_maior = indice

        if temperatura_atual < menor:

            menor = temperatura_atual

            indice_menor = indice

    media = soma / len(temperaturas)

    # Verificar os que Estão Acima da Media

    contador_acima_media = 0

    for indice in range(len(temperaturas)):

        temperatura_atual = temperaturas[indice]

        if temperatura_atual > media:

            contador_acima_media += 1

    # Retornar Resultados
    return (media, maior, menor, indice_maior, indice_menor, contador_acima_media)


# Fazer Analise das Temperaturas
media, maior, menor, indice_maior, indice_menor, contador_acima_media = (
    analisar_temperaturas(temperaturas)
)

# Mostrar Todos os Elementos
print("\nTemperaturas Armazenadas")

print("-" * 50)

for indice in range(len(temperaturas)):

    print(f"Indice {indice}: {temperaturas[indice]}°C")

print("-" * 50)

# Mostrar Resultados

print("Média das Temperaturas:", media)

print("Maior Temperatura:", maior)

print("Menor Temperatura:", menor)

print("Índice da Maior Temperatura:", indice_maior)

print("Índice da Menor Temperatura:", indice_menor)

print("Quantidade Acima da Média:", contador_acima_media)

# O array foi percorrido aproximadamente duas vezes.
# No primeiro percurso foram analisadas as 10 temperaturas para calcular a soma, o maior e o menor valor.
# No segundo percurso, as 10 temperaturas foram verificadas novamente para identificar quais estavam acima da média.
# Portanto, foram realizados aproximadamente 20 percursos de elementos.

# Complexidade

# A complexidade é:

# O(n)
# Porque, mesmo tendo dois for separados, eles não estão um dentro do outro.
# n + n = 2n
# Na análise de complexidade, constantes são ignoradas:
# O(2n) → O(n)
