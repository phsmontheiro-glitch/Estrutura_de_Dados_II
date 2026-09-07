# PARTE 3 - RESULTADOS DA INVESTIGAÇÃO DE BUSCA EM MATRIZES

## Objetivo

Nesta parte da atividade foi realizado um experimento utilizando o algoritmo de busca sequencial em matrizes.

O objetivo foi observar como o tamanho da matriz e a posição do elemento procurado influenciam a quantidade de comparações realizadas.

A busca foi implementada utilizando loops aninhados para percorrer as linhas e colunas das matrizes.

Foram realizados testes com as seguintes matrizes:

- Matriz 2 × 2;
- Matriz 10 × 10;
- Matriz 100 × 100.

Para cada matriz foram analisadas três situações:

1. Valor localizado no início da matriz;
2. Valor localizado próximo ao final da matriz;
3. Valor inexistente na matriz.

Durante os testes foram registrados:

- Valor procurado;
- Se o valor foi encontrado;
- Linha;
- Coluna;
- Quantidade de comparações realizadas.

---

# Tabela de Resultados

| Matriz | Nº de elementos | Busca no início | Busca próximo ao final | Valor inexistente |
|---|---:|---:|---:|---:|
| 2 × 2 | 4 | 1 comparação | 3 comparações | 4 comparações |
| 10 × 10 | 100 | 1 comparação | 99 comparações | 100 comparações |
| 100 × 100 | 10.000 | 1 comparação | 9.999 comparações | 10.000 comparações |

> Os valores apresentados representam a quantidade de comparações realizadas durante a busca sequencial.

---

# Resultados dos Testes

## Matriz 2 × 2

A matriz possui:

```text
2 × 2 = 4 elementos
```

### Teste: Valor no início

```text
Valor procurado: 1

Valor encontrado: True

Linha: 0

Coluna: 0

Quantidade de comparações: 1
```

O valor foi encontrado imediatamente na primeira posição da matriz.

---

### Teste: Valor próximo ao final

```text
Valor procurado: 3

Valor encontrado: True

Linha: 1

Coluna: 0

Quantidade de comparações: 3
```

Foram necessárias 3 comparações até encontrar o valor.

---

### Teste: Valor inexistente

```text
Valor procurado: 5

Valor encontrado: False

Linha: None

Coluna: None

Quantidade de comparações: 4
```

Como o valor não existe na matriz, foi necessário percorrer todos os 4 elementos.

---

# Matriz 10 × 10

A matriz possui:

```text
10 × 10 = 100 elementos
```

### Teste: Valor no início

```text
Valor procurado: 1

Valor encontrado: True

Linha: 0

Coluna: 0

Quantidade de comparações: 1
```

O valor foi encontrado na primeira posição da matriz.

---

### Teste: Valor próximo ao final

```text
Valor procurado: 99

Valor encontrado: True

Linha: 9

Coluna: 8

Quantidade de comparações: 99
```

Como o valor estava localizado próximo ao final da matriz, foi necessário realizar 99 comparações.

---

### Teste: Valor inexistente

```text
Valor procurado: 101

Valor encontrado: False

Linha: None

Coluna: None

Quantidade de comparações: 100
```

Como o valor não existe na matriz, todos os 100 elementos foram percorridos.

---

# Matriz 100 × 100

A matriz possui:

```text
100 × 100 = 10.000 elementos
```

### Teste: Valor no início

```text
Valor procurado: 1

Valor encontrado: True

Linha: 0

Coluna: 0

Quantidade de comparações: 1
```

O valor foi encontrado imediatamente na primeira posição.

Mesmo sendo uma matriz com 10.000 elementos, apenas uma comparação foi necessária porque o elemento estava no início.

---

### Teste: Valor próximo ao final

```text
Valor procurado: 9999

Valor encontrado: True

Linha: 99

Coluna: 98

Quantidade de comparações: 9.999
```

Como o valor estava localizado próximo ao final da matriz, praticamente todos os elementos anteriores precisaram ser comparados.

---

### Teste: Valor inexistente

```text
Valor procurado: 10001

Valor encontrado: False

Linha: None

Coluna: None

Quantidade de comparações: 10.000
```

Como o valor procurado não existe na matriz, foi necessário percorrer todos os seus elementos.

Esse representa o pior comportamento observado nos experimentos.

---

# Análise dos Resultados

## a) Por que encontrar um elemento no início exige menos operações?

Encontrar um elemento no início exige menos operações porque a busca sequencial percorre os elementos na ordem em que estão armazenados.

Quando o valor procurado está na primeira posição, o algoritmo realiza apenas uma comparação.

Isso foi observado em todas as matrizes utilizadas:

```text
Matriz 2 × 2:

1 comparação


Matriz 10 × 10:

1 comparação


Matriz 100 × 100:

1 comparação
```

Portanto, mesmo que a matriz possua uma grande quantidade de elementos, encontrar um valor logo no início exige poucas operações.

---

## b) O que acontece quando o elemento procurado não existe?

Quando o elemento procurado não existe, a busca sequencial precisa percorrer toda a matriz.

O algoritmo só consegue concluir que o valor não está presente depois de comparar todos os elementos.

Nos experimentos realizados:

```text
Matriz 2 × 2:

4 comparações


Matriz 10 × 10:

100 comparações


Matriz 100 × 100:

10.000 comparações
```

Isso demonstra que, quando o valor não existe, a quantidade de comparações é igual à quantidade total de elementos da matriz.

---

## c) Qual é o pior caso da busca sequencial?

O pior caso da busca sequencial acontece quando:

- O elemento procurado não existe na estrutura;

ou quando:

- O elemento está localizado na última posição percorrida pelo algoritmo.

Nessas situações, o algoritmo precisa percorrer praticamente todos ou todos os elementos da estrutura.

Nos experimentos realizados, o maior número de comparações ocorreu na busca por um valor inexistente.

Por exemplo:

```text
Matriz 100 × 100:

10.000 elementos

10.000 comparações
```

Portanto, o pior caso ocorre quando é necessário percorrer toda a estrutura.

---

## d) Como o aumento das dimensões da matriz influencia a quantidade de operações?

O aumento das dimensões da matriz aumenta a quantidade total de elementos que podem precisar ser percorridos.

Nos experimentos foram utilizadas:

```text
2 × 2
↓
4 elementos


10 × 10
↓
100 elementos


100 × 100
↓
10.000 elementos
```

Quando o elemento está no início, o número de comparações pode continuar pequeno.

Porém, quando o elemento está próximo ao final ou não existe, o aumento da matriz influencia diretamente a quantidade de operações.

Isso pode ser observado nos resultados:

```text
Busca por valor inexistente:

2 × 2:

4 comparações


10 × 10:

100 comparações


100 × 100:

10.000 comparações
```

Portanto, quanto maior a quantidade de elementos presentes na matriz, maior pode ser a quantidade de comparações necessárias.

Existe uma relação entre:

```text
Número de linhas
        ×
Número de colunas
        ↓
Quantidade de elementos
        ↓
Quantidade de comparações
        ↓
Custo computacional
```

---

## e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas?

Em uma matriz com:

```text
m linhas

n colunas
```

A quantidade total de elementos é:

```text
m × n
```

No pior caso, a busca sequencial pode precisar percorrer todos os elementos.

Portanto, sua complexidade é:

```text
O(m × n)
```

Quando a matriz é quadrada e possui aproximadamente `n × n` elementos, essa complexidade pode ser representada como:

```text
O(n²)
```

Isso ocorre porque existem dois percursos realizados pelos loops aninhados:

```text
Loop das linhas
        ↓
Para cada linha
        ↓
Loop das colunas
        ↓
Percorre os elementos da matriz
```

---

# Conclusão do Experimento

Os experimentos demonstraram que a quantidade de comparações realizadas pela busca sequencial depende diretamente da posição do elemento procurado e do tamanho da matriz.

Quando o elemento estava localizado no início, apenas uma comparação foi necessária em todas as matrizes.

Por outro lado, quando o elemento estava próximo ao final, foi necessário percorrer praticamente toda a estrutura.

O maior número de comparações ocorreu quando o valor procurado não existia na matriz.

Os resultados demonstram claramente a relação entre:

```text
Tamanho da matriz
        ↓
Quantidade de elementos
        ↓
Posição do elemento procurado
        ↓
Quantidade de comparações
        ↓
Complexidade computacional
```

Na matriz 2 × 2, o pior caso exigiu 4 comparações.

Na matriz 10 × 10, o pior caso exigiu 100 comparações.

Na matriz 100 × 100, o pior caso exigiu 10.000 comparações.

Dessa forma, foi possível observar experimentalmente que o aumento da estrutura de dados pode aumentar significativamente a quantidade de operações necessárias.

A busca sequencial possui complexidade:

```text
O(m × n)
```

pois, no pior caso, é necessário percorrer todas as linhas e todas as colunas da matriz.

Portanto, a atividade demonstrou que não basta verificar apenas se um valor foi encontrado ou não.

Também é importante analisar quantas operações foram necessárias para chegar ao resultado.

Assim, diferentes tamanhos de entrada podem produzir comportamentos muito diferentes em relação à quantidade de operações e ao custo computacional do algoritmo.

