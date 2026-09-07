# PARTE 2 - RESULTADOS DO EXPERIMENTO DE ORDENAÇÃO

## Objetivo

Nesta parte foi realizado um experimento para comparar os algoritmos de ordenação Bubble Sort e Quick Sort.

Os testes foram realizados utilizando arrays de diferentes tamanhos:

- 10 elementos;
- 20 elementos;
- 1.000 elementos.

Para garantir uma comparação justa, foram utilizados exatamente os mesmos dados para os dois algoritmos.

A partir de um mesmo array original, foram criadas cópias separadas:

```text
Array original
        ↓
   ┌─────────┐
   │ Cópia 1 │ → Bubble Sort
   └─────────┘

   ┌─────────┐
   │ Cópia 2 │ → Quick Sort
   └─────────┘
```

Durante a execução foram contabilizadas as operações realizadas pelos algoritmos.

Foram analisadas:

- Comparações;
- Trocas realizadas pelo Bubble Sort;
- Movimentações realizadas pelo Quick Sort.

---

# Tabela de Resultados

| Tamanho do Array | Bubble Sort - Comparações | Bubble Sort - Trocas | Quick Sort - Comparações | Quick Sort - Movimentações |
|---|---:|---:|---:|---:|
| 10 elementos | 39 | 17 | 25 | 13 |
| 20 elementos | 187 | 96 | 71 | 30 |
| 1.000 elementos | 499.175 | 243.275 | 10.910 | 4.616 |

> Os valores apresentados na tabela foram obtidos experimentalmente durante a execução do programa.

---

# Análise dos Resultados

## a) Qual algoritmo realizou menos operações para 10 elementos?

Para o array de 10 elementos, os resultados obtidos foram:

```text
Bubble Sort:

Comparações: 39
Trocas: 17


Quick Sort:

Comparações: 25
Movimentações: 13
```

Considerando as operações contabilizadas, o algoritmo que apresentou menor quantidade de operações foi o **Quick Sort**.

O Bubble Sort realizou:

```text
39 comparações + 17 trocas = 56 operações contabilizadas
```

O Quick Sort realizou:

```text
25 comparações + 13 movimentações = 38 operações contabilizadas
```

Portanto, no experimento com 10 elementos, o Quick Sort realizou menos operações.

Mesmo sendo um array pequeno, já foi possível observar uma diferença entre os dois algoritmos.

---

## b) O comportamento permaneceu igual para 20 elementos?

Sim.

Ao aumentar o tamanho do array para 20 elementos, o Quick Sort continuou apresentando uma quantidade menor de operações.

Os resultados foram:

```text
Bubble Sort:

Comparações: 187
Trocas: 96


Quick Sort:

Comparações: 71
Movimentações: 30
```

Considerando as operações contabilizadas:

```text
Bubble Sort:

187 comparações + 96 trocas = 283 operações


Quick Sort:

71 comparações + 30 movimentações = 101 operações
```

Portanto, o comportamento permaneceu igual, pois o Quick Sort continuou realizando menos operações que o Bubble Sort.

Além disso, a diferença entre os algoritmos se tornou mais perceptível quando o tamanho do array aumentou de 10 para 20 elementos.

---

## c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?

Quando o tamanho do array aumentou para 1.000 elementos, a diferença na quantidade de operações se tornou muito mais evidente.

Os resultados foram:

```text
Bubble Sort:

Comparações: 499.175
Trocas: 243.275


Quick Sort:

Comparações: 10.910
Movimentações: 4.616
```

Considerando as operações contabilizadas:

```text
Bubble Sort:

499.175 comparações + 243.275 trocas
= 742.450 operações


Quick Sort:

10.910 comparações + 4.616 movimentações
= 15.526 operações
```

O Bubble Sort precisou realizar uma quantidade muito maior de operações.

Isso acontece porque sua estratégia consiste em comparar elementos vizinhos repetidamente e realizar trocas sempre que necessário.

Já o Quick Sort utiliza uma estratégia baseada na escolha de um pivô e na divisão do problema em partes menores.

No experimento com 1.000 elementos, a diferença foi bastante significativa.

O Bubble Sort realizou centenas de milhares de operações, enquanto o Quick Sort realizou uma quantidade muito menor.

---

## d) Qual algoritmo apresentou maior crescimento da quantidade de operações?

O algoritmo que apresentou maior crescimento na quantidade de operações foi o **Bubble Sort**.

Considerando os resultados obtidos:

```text
10 elementos:

Bubble Sort: 56 operações
Quick Sort: 38 operações


20 elementos:

Bubble Sort: 283 operações
Quick Sort: 101 operações


1.000 elementos:

Bubble Sort: 742.450 operações
Quick Sort: 15.526 operações
```

É possível observar que, conforme o tamanho do array aumentou, a quantidade de operações realizadas pelo Bubble Sort cresceu muito mais rapidamente.

Isso está relacionado à sua complexidade no caso médio e no pior caso:

```text
O(n²)
```

Quando o tamanho da entrada aumenta, a quantidade de comparações e possíveis trocas pode crescer de forma quadrática.

O Quick Sort possui, no caso médio:

```text
O(n log n)
```

Por esse motivo, geralmente apresenta um crescimento mais eficiente quando a quantidade de elementos aumenta.

---

## e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?

Sim.

Os resultados experimentais são coerentes com as complexidades teóricas estudadas.

O Bubble Sort possui:

```text
Melhor caso:

O(n)


Caso médio:

O(n²)


Pior caso:

O(n²)
```

Já o Quick Sort possui:

```text
Melhor caso:

O(n log n)


Caso médio:

O(n log n)


Pior caso:

O(n²)
```

Nos testes realizados, foi possível observar que o aumento do tamanho do array influenciou diretamente a quantidade de operações realizadas.

A diferença entre os algoritmos se tornou muito mais evidente no teste com 1.000 elementos.

Enquanto o Bubble Sort realizou:

```text
742.450 operações contabilizadas
```

O Quick Sort realizou:

```text
15.526 operações contabilizadas
```

Isso demonstra, na prática, a relação entre:

```text
Tamanho da entrada
        ↓
Quantidade de operações
        ↓
Complexidade computacional
        ↓
Eficiência do algoritmo
```

Portanto, os resultados experimentais estão de acordo com o comportamento esperado pelas complexidades teóricas estudadas.

---

## f) Em qual situação você escolheria Bubble Sort?

O Bubble Sort pode ser escolhido em situações como:

- Arrays pequenos;
- Fins educacionais;
- Aprendizado de algoritmos de ordenação;
- Situações simples;
- Quando o desempenho não é uma prioridade.

O Bubble Sort possui uma lógica simples e fácil de entender.

Porém, não é recomendado para grandes quantidades de dados devido ao crescimento da quantidade de comparações e trocas.

No experimento realizado, isso ficou evidente no array de 1.000 elementos.

---

## g) Em qual situação você escolheria Quick Sort?

O Quick Sort pode ser escolhido em situações como:

- Arrays maiores;
- Grandes quantidades de dados;
- Situações onde o desempenho é importante;
- Problemas que exigem uma ordenação mais eficiente;
- Quando é possível utilizar uma boa estratégia para escolher o pivô.

O Quick Sort geralmente apresenta melhor desempenho para grandes quantidades de elementos devido à sua estratégia de dividir o problema em partes menores.

No caso médio, sua complexidade é:

```text
O(n log n)
```

No experimento realizado, isso ficou evidente principalmente no teste com 1.000 elementos.

---

# Conclusão do Experimento

Os experimentos demonstraram que dois algoritmos podem produzir exatamente o mesmo resultado final, ou seja, um array ordenado.

Porém, a quantidade de operações realizadas para chegar até esse resultado pode ser completamente diferente.

No experimento com 10 elementos, o Bubble Sort realizou 56 operações contabilizadas, enquanto o Quick Sort realizou 38.

No experimento com 20 elementos, o Bubble Sort realizou 283 operações, enquanto o Quick Sort realizou 101.

A maior diferença foi observada no experimento com 1.000 elementos.

```text
Bubble Sort:

742.450 operações


Quick Sort:

15.526 operações
```

O Bubble Sort utiliza comparações entre elementos vizinhos e pode realizar muitas comparações e trocas.

O Quick Sort utiliza uma estratégia baseada em um pivô e na divisão do problema em partes menores.

À medida que o tamanho do array aumenta, a diferença entre a quantidade de operações realizadas pelos algoritmos se torna muito mais evidente.

Portanto, não é suficiente analisar apenas o resultado final da ordenação.

Também é necessário analisar:

```text
Tamanho do array
        ↓
Quantidade de comparações
        ↓
Quantidade de trocas ou movimentações
        ↓
Complexidade computacional
        ↓
Eficiência do algoritmo
```

Dessa forma, foi possível observar experimentalmente que algoritmos diferentes podem resolver o mesmo problema, mas apresentar custos computacionais diferentes quando o tamanho da entrada aumenta.

