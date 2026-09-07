# PARTE 4 - ANÁLISE DO ARRAY DE TEMPERATURAS

## Objetivo

Nesta parte da atividade foi desenvolvido um programa utilizando um array para armazenar 10 temperaturas.

O objetivo foi aplicar conceitos de:

- Arrays;
- Índices;
- Loops;
- Percurso de estruturas de dados;
- Cálculo de média;
- Identificação do maior e menor valor;
- Análise da quantidade de operações;
- Complexidade computacional.

O programa recebe 10 temperaturas, armazena os valores em um array e realiza diferentes análises sobre os dados.

---

# Temperaturas Informadas

Durante a execução do programa foram informadas as seguintes temperaturas:

```text
Índice 0: 23.5°C
Índice 1: 34.0°C
Índice 2: 1.0°C
Índice 3: 45.0°C
Índice 4: 12.0°C
Índice 5: 68.0°C
Índice 6: 12.0°C
Índice 7: 34.0°C
Índice 8: 22.0°C
Índice 9: 19.0°C
```

A representação do array pode ser observada da seguinte forma:

```text
Índice:        0     1    2     3     4     5     6     7     8     9

Temperatura:  23.5  34.0  1.0  45.0  12.0  68.0  12.0  34.0  22.0  19.0
```

---

# Resultados Obtidos

Após percorrer o array e realizar os cálculos, foram obtidos os seguintes resultados:

```text
Média das Temperaturas: 27.05°C

Maior Temperatura: 68.0°C

Menor Temperatura: 1.0°C

Índice da Maior Temperatura: 5

Índice da Menor Temperatura: 2

Quantidade Acima da Média: 4
```

---

# Análise dos Resultados

## Média das Temperaturas

A média das 10 temperaturas informadas foi:

```text
27.05°C
```

Para calcular a média, foi necessário percorrer os elementos do array e somar todos os valores.

Depois da soma, o resultado foi dividido pela quantidade de temperaturas armazenadas.

De forma simplificada:

```text
Soma das temperaturas
        ↓
Divisão pela quantidade de elementos
        ↓
Média das temperaturas
```

---

## Maior Temperatura

A maior temperatura encontrada no array foi:

```text
68.0°C
```

Esse valor está localizado no:

```text
Índice 5
```

Durante o percurso do array, cada temperatura foi comparada com o maior valor encontrado até aquele momento.

Quando uma temperatura maior era encontrada, o valor da maior temperatura e seu índice eram atualizados.

---

## Menor Temperatura

A menor temperatura encontrada foi:

```text
1.0°C
```

Esse valor está localizado no:

```text
Índice 2
```

Durante o percurso do array, cada temperatura foi comparada com o menor valor encontrado até aquele momento.

Quando uma temperatura menor era encontrada, o valor da menor temperatura e seu índice eram atualizados.

---

## Temperaturas Acima da Média

A média calculada foi:

```text
27.05°C
```

Foram encontradas:

```text
4 temperaturas acima da média
```

Os valores acima da média foram:

```text
34.0°C

45.0°C

68.0°C

34.0°C
```

Para realizar essa contagem, foi necessário percorrer novamente os elementos do array e comparar cada temperatura com a média calculada.

---

# Quantidade Aproximada de Operações de Percurso

O array possui:

```text
10 elementos
```

Para realizar todas as análises, o programa precisa percorrer o array.

Considerando as principais etapas:

```text
Entrada das temperaturas:

10 posições percorridas


Exibição das temperaturas:

10 posições percorridas


Cálculo da média:

10 posições percorridas


Identificação do maior e menor valor:

10 posições percorridas


Contagem de valores acima da média:

10 posições percorridas
```

Portanto, aproximadamente:

```text
10
+
10
+
10
+
10
+
10
=
50 operações de percurso
```

Esse número é uma estimativa baseada nas principais etapas que percorrem o array.

A quantidade exata de operações pode variar dependendo da forma como o código foi implementado, pois existem também atribuições, comparações, cálculos e acessos aos índices.

Entretanto, o ponto principal é que cada etapa percorre uma quantidade proporcional ao número de elementos armazenados.

---

# Relação Entre o Tamanho do Array e as Operações

Se o número de temperaturas aumentasse, a quantidade de elementos que precisariam ser percorridos também aumentaria.

Por exemplo:

```text
10 temperaturas
        ↓
Aproximadamente 50 percursos considerando 5 etapas


100 temperaturas
        ↓
Aproximadamente 500 percursos considerando as mesmas etapas


1.000 temperaturas
        ↓
Aproximadamente 5.000 percursos considerando as mesmas etapas
```

Isso demonstra que o crescimento da quantidade de operações é proporcional ao tamanho do array.

---

# Complexidade Computacional

As principais operações realizadas no programa percorrem o array uma quantidade proporcional ao número de elementos.

Por exemplo:

- Receber as temperaturas;
- Exibir as temperaturas;
- Calcular a média;
- Encontrar o maior valor;
- Encontrar o menor valor;
- Contar valores acima da média.

Cada um desses percursos possui complexidade:

```text
O(n)
```

Mesmo que o programa percorra o array mais de uma vez, a quantidade de percursos é constante.

Por exemplo:

```text
O(n) + O(n) + O(n) + O(n) + O(n)
```

Pode ser simplificado para:

```text
O(n)
```

Portanto, a complexidade geral do algoritmo é:

```text
O(n)
```

Isso significa que, conforme a quantidade de temperaturas aumenta, a quantidade de operações cresce de forma aproximadamente proporcional.

---

# Conclusão

O experimento permitiu aplicar os conceitos de arrays, índices e loops utilizando um problema prático de análise de temperaturas.

Foram armazenadas 10 temperaturas e, a partir dos dados informados, foi possível calcular a média, identificar o maior e o menor valor, localizar seus respectivos índices e contar quantas temperaturas ficaram acima da média.

Os resultados obtidos foram:

```text
Média: 27.05°C

Maior temperatura: 68.0°C

Índice da maior temperatura: 5

Menor temperatura: 1.0°C

Índice da menor temperatura: 2

Temperaturas acima da média: 4
```

Também foi possível observar que diferentes operações exigem o percurso do array.

Embora o array seja percorrido mais de uma vez, a quantidade de percursos realizados pelo algoritmo permanece constante.

Portanto, o crescimento da quantidade de operações acompanha o aumento da quantidade de elementos.

Essa relação pode ser representada da seguinte forma:

```text
Quantidade de temperaturas
        ↓
Quantidade de posições percorridas
        ↓
Quantidade de operações
        ↓
Complexidade O(n)
```

Dessa forma, a atividade demonstrou que arrays permitem armazenar e analisar conjuntos de dados utilizando índices e loops, e que o custo computacional das operações depende diretamente da quantidade de elementos presentes na estrutura.

