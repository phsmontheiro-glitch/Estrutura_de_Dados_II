# PARTE 6 - ANÁLISE E CONCLUSÃO

## Análise dos Experimentos

Nesta atividade foram realizados experimentos utilizando arrays, matrizes, algoritmos de ordenação e algoritmos de busca.

O objetivo principal foi observar que diferentes algoritmos podem produzir o mesmo resultado, mas realizar quantidades diferentes de operações para chegar até esse resultado.

Durante os experimentos, foram analisados os algoritmos Bubble Sort e Quick Sort utilizando arrays de diferentes tamanhos.

Também foram realizados testes de busca sequencial em matrizes de diferentes dimensões, além da análise de arrays de temperaturas e de uma matriz utilizada para representar medições de sensores.

---

# 1. O aumento do tamanho da estrutura de dados influencia a quantidade de operações?

Sim.

O aumento do tamanho da estrutura de dados influencia diretamente a quantidade de operações realizadas pelos algoritmos.

Quando um array ou matriz possui mais elementos, é necessário realizar mais comparações, percorrer mais posições e, dependendo do algoritmo, realizar mais trocas ou movimentações.

Nos experimentos de ordenação, os arrays utilizados possuíam:

```text
10 elementos
20 elementos
1.000 elementos
```

Ao aumentar a quantidade de elementos, a quantidade de operações necessárias para ordenar os arrays também aumentou.

Esse comportamento também foi observado na busca sequencial em matrizes.

Foram utilizadas matrizes de:

```text
2 × 2 = 4 elementos

10 × 10 = 100 elementos

100 × 100 = 10.000 elementos
```

Quanto maior a quantidade de elementos presentes na matriz, maior pode ser a quantidade de comparações necessárias para encontrar um valor ou determinar que ele não existe.

Portanto, existe uma relação direta entre:

```text
Tamanho da estrutura
        ↓
Quantidade de elementos
        ↓
Quantidade de operações
        ↓
Custo computacional
```

---

# 2. Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?

Não.

Os dois algoritmos podem produzir o mesmo resultado final, ou seja, um array ordenado.

Entretanto, eles utilizam estratégias diferentes e, por isso, a quantidade de operações cresce de maneiras diferentes.

O Bubble Sort possui, no caso médio e no pior caso, complexidade:

```text
O(n²)
```

Isso significa que, quando o número de elementos aumenta, a quantidade de comparações pode crescer de forma quadrática.

Por exemplo, ao aumentar significativamente o tamanho de um array, o Bubble Sort tende a realizar uma quantidade muito maior de comparações e trocas.

O Quick Sort possui, no caso médio, complexidade:

```text
O(n log n)
```

Sua estratégia consiste em escolher um pivô e dividir o problema em partes menores.

Quando as divisões são relativamente equilibradas, o Quick Sort consegue ordenar grandes quantidades de dados utilizando menos operações do que o Bubble Sort.

Portanto, o crescimento dos algoritmos pode ser representado de forma simplificada:

```text
Bubble Sort
O(n²)
Crescimento quadrático
        ↓
A quantidade de operações aumenta rapidamente.


Quick Sort
O(n log n)
Crescimento mais eficiente no caso médio
        ↓
A quantidade de operações cresce mais lentamente.
```

Os experimentos com arrays de 10, 20 e 1.000 elementos permitem observar essa diferença.

Para arrays pequenos, a diferença entre os algoritmos pode não ser tão grande.

Entretanto, quando o número de elementos aumenta para 1.000, a diferença na quantidade de operações tende a se tornar muito mais evidente.

---

# 3. Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?

Analisar apenas o resultado final não é suficiente porque dois algoritmos diferentes podem produzir exatamente o mesmo array ordenado.

Por exemplo:

```text
Array original:

7, 3, 5
```

Após a ordenação, tanto o Bubble Sort quanto o Quick Sort podem produzir:

```text
3, 5, 7
```

O resultado final é igual.

Porém, o caminho utilizado para chegar até esse resultado é diferente.

O Bubble Sort organiza os elementos comparando posições vizinhas e realizando trocas quando necessário.

O Quick Sort escolhe um pivô e divide os elementos em partes menores e maiores em relação a esse pivô.

Como consequência, os algoritmos podem realizar quantidades diferentes de:

- Comparações;
- Trocas;
- Movimentações;
- Operações de percurso.

Por esse motivo, dois algoritmos podem estar corretos e produzir o mesmo resultado, mas um deles pode ser muito mais eficiente do que o outro.

A comparação entre algoritmos deve considerar não apenas:

```text
Resultado final
```

Mas também:

```text
Tamanho da entrada
        ↓
Quantidade de comparações
        ↓
Quantidade de trocas ou movimentações
        ↓
Complexidade computacional
        ↓
Eficiência do algoritmo
```

---

# CONCLUSÃO

A realização dos experimentos permitiu observar, na prática, a relação entre estruturas de dados, quantidade de operações e complexidade computacional.

Foi possível perceber que o aumento do tamanho de um array ou matriz influencia diretamente a quantidade de operações necessárias para percorrer, buscar ou organizar os elementos.

Na comparação entre os algoritmos de ordenação, foi observado que Bubble Sort e Quick Sort possuem estratégias diferentes.

O Bubble Sort utiliza comparações entre elementos vizinhos e pode realizar muitas comparações e trocas quando a quantidade de elementos aumenta.

Sua complexidade média e de pior caso é:

```text
O(n²)
```

O Quick Sort utiliza uma estratégia baseada na escolha de um pivô e na divisão do problema em partes menores.

No caso médio, sua complexidade é:

```text
O(n log n)
```

Essa diferença faz com que o Quick Sort geralmente seja mais eficiente para arrays maiores.

Nos experimentos com busca sequencial em matrizes, também foi possível observar que a posição do elemento influencia diretamente a quantidade de comparações.

Um elemento localizado no início da matriz pode ser encontrado rapidamente.

Por outro lado, um elemento localizado próximo ao final ou um valor inexistente pode exigir o percurso de grande parte ou de toda a matriz.

Nos exercícios de análise de temperaturas e monitoramento de sensores, foi possível aplicar conceitos de arrays, matrizes, índices e loops.

Os loops foram utilizados para percorrer cada elemento das estruturas e realizar cálculos como média, maior valor, menor valor e quantidade de valores acima de determinados limites.

Portanto, a atividade demonstrou que não é suficiente verificar apenas se um algoritmo funciona ou se produz o resultado correto.

Também é necessário analisar a quantidade de operações necessárias para chegar ao resultado.

Dessa forma, a eficiência de um algoritmo está relacionada diretamente com:

```text
Tamanho da entrada
        ↓
Quantidade de operações
        ↓
Complexidade computacional
        ↓
Desempenho e eficiência
```

Assim, foi possível compreender que diferentes algoritmos podem resolver o mesmo problema, mas apresentar comportamentos e custos computacionais completamente diferentes quando o tamanho da entrada aumenta.

