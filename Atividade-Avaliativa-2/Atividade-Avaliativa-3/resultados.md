# Resultados – Análise de Algoritmos de Ordenação

## Objetivo

Nesta etapa foram executados os algoritmos **Bubble Sort, Insertion Sort, Selection Sort e Quick Sort** utilizando os mesmos dados iniciais para cada tamanho de vetor.

Foram realizados testes com:

- 10 elementos;
- 20 elementos;
- 1.000 elementos.

O objetivo foi comparar a quantidade de **comparações** e **trocas ou movimentações** realizadas por cada algoritmo.

---

## Critério de contagem

Foram consideradas:

- **Comparações:** operações utilizadas para verificar a relação entre dois elementos.
- **Trocas:** troca de posição entre dois elementos.
- **Movimentações:** deslocamento ou reposicionamento de elementos durante a ordenação.

Cada algoritmo recebeu uma cópia do mesmo vetor original em cada experimento.

---

## Resultados

| Tamanho | Bubble Comparações | Bubble Trocas | Insertion Comparações | Insertion Mov. | Selection Comparações | Selection Trocas | Quick Comparações | Quick Mov. |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 35 | 20 | 28 | 29 | 45 | 8 | 21 | 10 |
| 20 | 189 | 113 | 130 | 132 | 190 | 17 | 72 | 25 |
| 1.000 | 498.324 | 251.723 | 252.710 | 252.722 | 499.500 | 994 | 10.965 | 5.220 |

---

# Análise dos resultados

## a) Qual algoritmo realizou o menor número de comparações para 10 elementos?

Para 10 elementos, o **Quick Sort** realizou o menor número de comparações.

Os resultados foram:

- Bubble Sort: 35 comparações;
- Insertion Sort: 28 comparações;
- Selection Sort: 45 comparações;
- Quick Sort: 21 comparações.

Portanto, o Quick Sort apresentou o menor número, com **21 comparações**.

---

## b) Qual algoritmo realizou menos trocas ou movimentações?

Para 10 elementos, o **Selection Sort** realizou a menor quantidade de trocas, com apenas **8 trocas**.

Os resultados foram:

- Bubble Sort: 20 trocas;
- Insertion Sort: 29 movimentações;
- Selection Sort: 8 trocas;
- Quick Sort: 10 movimentações.

---

## c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?

De maneira geral, sim.

O Quick Sort continuou apresentando uma quantidade menor de comparações:

- 10 elementos: 21 comparações;
- 20 elementos: 72 comparações.

O Insertion Sort também apresentou menos comparações que Bubble Sort e Selection Sort nos dois tamanhos.

Já Bubble Sort e Selection Sort apresentaram uma quantidade maior de comparações.

---

## d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?

Quando o vetor aumentou para 1.000 elementos, a diferença entre os algoritmos ficou muito maior.

Os resultados de comparações foram:

- Bubble Sort: **498.324**;
- Insertion Sort: **252.710**;
- Selection Sort: **499.500**;
- Quick Sort: **10.965**.

O Quick Sort realizou uma quantidade de comparações muito menor que os outros algoritmos.

Isso demonstra como o aumento do tamanho da entrada pode causar um crescimento significativo na quantidade de operações.

---

## e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade O(n²). Eles apresentaram exatamente a mesma quantidade de operações?

Não.

Apesar de Bubble Sort, Insertion Sort e Selection Sort apresentarem complexidade **O(n²)** em suas situações gerais, isso não significa que realizem exatamente a mesma quantidade de operações.

Com 1.000 elementos, por exemplo:

- Bubble Sort: 498.324 comparações;
- Insertion Sort: 252.710 comparações;
- Selection Sort: 499.500 comparações.

Portanto, algoritmos com a mesma ordem de complexidade podem apresentar quantidades diferentes de operações.

---

## f) Qual algoritmo apresentou maior crescimento no número de operações?

O **Bubble Sort** apresentou o maior crescimento na quantidade total de operações contabilizadas.

Considerando comparações e trocas/movimentações:

- Bubble Sort: **55 operações** com 10 elementos e **750.047 operações** com 1.000;
- Insertion Sort: **57 operações** com 10 elementos e **505.432 operações** com 1.000;
- Selection Sort: **53 operações** com 10 elementos e **500.494 operações** com 1.000;
- Quick Sort: **31 operações** com 10 elementos e **16.185 operações** com 1.000.

Assim, o Bubble Sort apresentou o maior crescimento na quantidade total de operações neste experimento.

---

## g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?

O Quick Sort apresentou um crescimento muito menor na quantidade de comparações conforme o tamanho do vetor aumentou.

Com 1.000 elementos, foram realizadas:

**10.965 comparações**

enquanto Bubble Sort e Selection Sort realizaram aproximadamente:

**499.000 comparações**.

Isso mostra uma diferença significativa de eficiência no experimento.

---

## h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?

Sim.

Bubble Sort, Insertion Sort e Selection Sort apresentaram um crescimento elevado da quantidade de operações conforme o tamanho do vetor aumentou.

O Quick Sort apresentou um crescimento significativamente menor.

Esse comportamento é coerente com as complexidades estudadas:

```text
Bubble Sort     → O(n²)
Insertion Sort  → O(n²)
Selection Sort  → O(n²)
Quick Sort      → O(n log n) em média
```

Os resultados experimentais demonstram, na prática, a diferença entre essas ordens de crescimento.

---

## i) Se você fosse responsável pelo sistema da central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria?

Eu escolheria o **Quick Sort**.

No experimento com 1.000 elementos, ele realizou apenas **10.965 comparações**, enquanto Bubble Sort e Selection Sort realizaram aproximadamente **499.000 comparações**.

Por apresentar um comportamento mais eficiente para grandes quantidades de dados e complexidade média **O(n log n)**, o Quick Sort seria uma escolha mais adequada para ordenar milhares de pedidos.

---

# Conclusão

O experimento mostrou que diferentes algoritmos podem produzir o mesmo resultado final, mas realizar quantidades muito diferentes de operações.

Nos testes realizados, a diferença ficou principalmente evidente quando o vetor passou para 1.000 elementos. Bubble Sort e Selection Sort apresentaram aproximadamente **499 mil comparações**, enquanto o Quick Sort realizou **10.965 comparações**.

O Insertion Sort também apresentou menos comparações que Bubble Sort e Selection Sort nesse conjunto de dados.

Assim, o experimento reforça a importância de analisar não apenas se um algoritmo funciona, mas também a quantidade de operações realizadas e sua complexidade.

```text
Tamanho da entrada
        ↓
Quantidade de operações
        ↓
Complexidade
        ↓
Eficiência
```
