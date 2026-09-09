# Desafio – Influência da Organização Inicial dos Dados

## Objetivo

Neste desafio foi analisado se a organização inicial dos dados influencia a quantidade de operações realizadas pelos algoritmos de ordenação.

Foram utilizados os algoritmos:

- Bubble Sort;
- Insertion Sort;
- Selection Sort;
- Quick Sort.

O experimento foi realizado com **1.000 elementos**, utilizando três situações diferentes:

1. Vetor aleatório;
2. Vetor já ordenado;
3. Vetor em ordem inversa.

Cada algoritmo recebeu uma cópia do mesmo vetor em cada situação, garantindo uma comparação justa.

---

## Como os vetores foram criados

Foi gerado um único vetor aleatório com 1.000 elementos. A partir dele foram criadas as versões ordenada e inversa:

```python
# Gera um vetor aleatório com 1.000 elementos
vetor_original = [
    random.randint(1, 10000)
    for _ in range(1000)
]

# Cria as três formas de organização
vetor_aleatorio = vetor_original.copy()
vetor_ordenado = sorted(vetor_original)
vetor_inverso = sorted(vetor_original, reverse=True)
```

Dessa forma, os três testes utilizam os mesmos valores, mudando apenas a organização dos elementos.

---

## Critério de contagem

Foram consideradas:

- **Comparações:** operações utilizadas para verificar a relação entre elementos.
- **Trocas:** troca de posição entre dois elementos.
- **Movimentações:** deslocamento ou reposicionamento de elementos durante a ordenação.

Os mesmos critérios utilizados no experimento principal foram mantidos neste desafio.

---

# Resultados

## Vetor aleatório

| Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 499.247 | 246.426 |
| Insertion Sort | 247.417 | 247.425 |
| Selection Sort | 499.500 | 989 |
| Quick Sort | 10.637 | 4.930 |

No vetor aleatório, o **Quick Sort** apresentou a menor quantidade de comparações, com apenas **10.637**.

---

## Vetor ordenado

| Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 999 | 0 |
| Insertion Sort | 999 | 999 |
| Selection Sort | 499.500 | 0 |
| Quick Sort | 499.500 | 0 |

No vetor já ordenado, o **Bubble Sort** apresentou apenas **999 comparações e nenhuma troca**.

O **Insertion Sort** também realizou apenas 999 comparações, porém contabilizou 999 movimentações ao posicionar os elementos.

O **Selection Sort** continuou realizando **499.500 comparações**.

O **Quick Sort** também apresentou **499.500 comparações**. Isso aconteceu porque o algoritmo utilizado escolhe o **último elemento como pivô**, o que gera um comportamento desfavorável quando o vetor já está ordenado.

---

## Vetor inverso

| Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 499.500 | 499.452 |
| Insertion Sort | 499.498 | 500.451 |
| Selection Sort | 499.500 | 525 |
| Quick Sort | 469.242 | 525 |

No vetor em ordem inversa, Bubble Sort e Insertion Sort apresentaram uma quantidade muito elevada de comparações e movimentações.

O **Selection Sort** manteve **499.500 comparações**, mas realizou apenas **525 trocas**.

O **Quick Sort** apresentou **469.242 comparações**, mostrando que sua quantidade de operações aumentou bastante em relação ao vetor aleatório.

---

# Análise geral

Os resultados mostram que a organização inicial dos dados **influencia os algoritmos de maneiras diferentes**.

### Bubble Sort

O Bubble Sort foi bastante beneficiado pelo vetor já ordenado.

Nesse caso, realizou:

- 999 comparações;
- 0 trocas.

No vetor inverso, porém, realizou quase 500 mil comparações e aproximadamente 500 mil trocas.

Isso demonstra que o Bubble Sort pode apresentar comportamentos muito diferentes dependendo da organização dos dados.

### Insertion Sort

O Insertion Sort também apresentou um comportamento muito favorável com o vetor já ordenado.

Foram realizadas apenas **999 comparações**.

Já no vetor inverso, o algoritmo realizou **499.498 comparações** e **500.451 movimentações**, mostrando um crescimento muito grande na quantidade de operações.

### Selection Sort

O Selection Sort apresentou praticamente a mesma quantidade de comparações nos três casos:

- Aleatório: 499.500;
- Ordenado: 499.500;
- Inverso: 499.500.

Isso acontece porque o algoritmo precisa procurar o menor elemento em cada posição, independentemente da organização inicial do vetor.

A quantidade de trocas, entretanto, variou.

### Quick Sort

O Quick Sort apresentou o melhor resultado no vetor aleatório, com apenas **10.637 comparações**.

Porém, no vetor ordenado, foram realizadas **499.500 comparações**.

No vetor inverso, foram realizadas **469.242 comparações**.

Essa diferença ocorre principalmente devido à estratégia de escolha do pivô utilizada no algoritmo. Neste experimento, o último elemento do vetor é utilizado como pivô.

---

# Comparação entre as situações

| Organização | Melhor comportamento observado | Maior destaque |
|---|---|---|
| Aleatório | Quick Sort | 10.637 comparações |
| Ordenado | Bubble Sort / Insertion Sort | 999 comparações |
| Inverso | Selection Sort em trocas | 525 trocas |

Os resultados mostram que **não existe um único algoritmo que apresente o melhor comportamento em todas as situações analisadas**.

O desempenho depende tanto do algoritmo quanto da organização inicial dos dados.

---

# Relação com a complexidade

Os resultados também ajudam a visualizar, na prática, as diferenças entre as complexidades teóricas.

O Bubble Sort, Insertion Sort e Selection Sort possuem comportamento **O(n²)** em seus casos gerais, mas a quantidade real de operações pode variar bastante dependendo da entrada e da implementação.

O Quick Sort possui complexidade média **O(n log n)**, mas pode chegar a **O(n²)** em situações desfavoráveis, como pode ser observado neste experimento com o vetor já ordenado.

---

# Conclusão

O desafio mostrou que a organização inicial dos dados influencia significativamente o desempenho dos algoritmos de ordenação.

O **Bubble Sort** e o **Insertion Sort** apresentaram excelente comportamento quando o vetor já estava ordenado, enquanto tiveram um grande aumento de operações no vetor inverso.

O **Selection Sort** manteve praticamente a mesma quantidade de comparações nos três casos, mostrando que sua estratégia é menos dependente da organização inicial dos dados.

O **Quick Sort** apresentou o melhor resultado no vetor aleatório, mas teve um comportamento muito pior nos vetores ordenado e inverso devido à escolha do último elemento como pivô.

Portanto, o experimento demonstra que, além de conhecer a complexidade teórica de um algoritmo, é importante considerar também a **organização dos dados de entrada e a implementação utilizada**.

