# Atividade Avaliativa 2 - Estrutura de Dados II

## Sobre a atividade

Esta atividade foi desenvolvida para a disciplina de **Estrutura de Dados II**, com o objetivo de estudar e aplicar conceitos fundamentais de estruturas de dados, algoritmos de ordenação, busca, arrays, matrizes, loops e complexidade computacional.

Durante a atividade foram desenvolvidos códigos e experimentos para observar, medir e analisar a quantidade de operações realizadas pelos algoritmos.

Como complemento, também foi realizada uma atividade prática de análise de algoritmos de ordenação, comparando **Bubble Sort, Insertion Sort, Selection Sort e Quick Sort** em diferentes situações de entrada.

---

## Conteúdos trabalhados

- Arrays
- Matrizes
- Índices
- Loops
- Loops aninhados
- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort
- Busca sequencial
- Comparações
- Trocas e movimentações
- Complexidade computacional
- Análise experimental de algoritmos
- Influência da organização inicial dos dados

---

## Estrutura do projeto

```text
Atividade-Avaliativa-2/
│
├── README.md
│
├── Parte-1-Pesquisa/
│   └── pesquisa.md
│
├── Parte-2-Ordenacao/
│   ├── ordenacao.py
│   └── resultados.md
│
├── Parte-3-Busca-em-Matrizes/
│   ├── busca_matrizes.py
│   └── resultados.md
│
├── Parte-4-Investigacao-do-Array/
│   ├── temperaturas.py
│   └── analise.md
│
├── Parte-5-Monitoramento-de-Sensores/
│   ├── sensores.py
│   └── analise.md
│
├── Parte-6-Analise-Conclusao/
│   └── analise.md
│
└── Atividade-3-Ordenacao/
    ├── ordenacao.py
    ├── resultados.md
    └── desafio.md
```

---

# Partes da atividade

## Parte 1 - Pesquisa

Foi realizada uma pesquisa sobre os algoritmos **Bubble Sort** e **Quick Sort**.

Foram analisados:

- funcionamento;
- lógica de ordenação;
- melhor caso;
- caso médio;
- pior caso;
- uso de memória;
- vantagens;
- limitações;
- situações de uso.

Também foi criada uma tabela comparativa entre os dois algoritmos.

📄 **[Acessar pesquisa](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-1-Pesquisa/pesquisa.md)**

---

## Parte 2 - Experimento de Ordenação

Foi desenvolvido um experimento para comparar os algoritmos **Bubble Sort** e **Quick Sort** utilizando os mesmos dados.

Foram realizados testes com arrays de:

- 10 elementos;
- 20 elementos;
- 1.000 elementos.

O programa contabiliza:

- comparações;
- trocas do Bubble Sort;
- movimentações do Quick Sort.

Além do código, foram registrados os resultados experimentais e realizadas as análises solicitadas pela atividade.

📄 **[Acessar código da ordenação](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-2-Ordenacao/ordenacao.py)**

📊 **[Acessar resultados e análise](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-2-Ordenacao/resultados.md)**

---

## Parte 3 - Busca em Matrizes

Foi desenvolvido um algoritmo de **busca sequencial utilizando loops aninhados**.

Foram utilizadas matrizes de:

- 2 × 2;
- 10 × 10;
- 100 × 100.

Em cada matriz foram realizados testes com:

- valor localizado no início;
- valor próximo ao final;
- valor inexistente.

Também foi contabilizada a quantidade de comparações realizadas.

📄 **[Acessar código da busca](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-3-Busca-em-Matrizes/busca_matrizes.py)**

📊 **[Acessar resultados e análise](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-3-Busca-em-Matrizes/resultados.md)**

---

## Parte 4 - Investigação do Array

Foi desenvolvido um programa utilizando um array com 10 temperaturas.

O programa realiza:

- entrada das temperaturas;
- exibição dos elementos;
- cálculo da média;
- identificação da maior temperatura;
- identificação da menor temperatura;
- identificação dos índices do maior e menor valor;
- contagem de valores acima da média.

Também foi analisada a quantidade aproximada de percursos realizados pelo array e a complexidade do algoritmo.

📄 **[Acessar código das temperaturas](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-4-Investigacao-do-Array/temperaturas.py)**

📊 **[Acessar análise](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-4-Investigacao-do-Array/analise.md)**

---

## Parte 5 - Monitoramento de Sensores

Foi desenvolvido um sistema utilizando uma matriz para representar:

**5 sensores × 24 medições = 120 temperaturas.**

O programa realiza:

- média de cada sensor;
- identificação da maior temperatura;
- identificação do sensor responsável pelo maior valor;
- identificação do horário da ocorrência;
- cálculo da média geral;
- contagem de leituras acima de um limite informado.

Também foram analisados os loops aninhados, os índices da matriz, a quantidade de posições percorridas e a relação entre as dimensões da matriz e a quantidade de operações.

📄 **[Acessar código dos sensores](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-5-Monitoramento-de-Sensores/sensores.py)**

📊 **[Acessar análise](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-5-Monitoramento-de-Sensores/analise.md)**

---

## Parte 6 - Análise e Conclusão

Nesta etapa foram analisados os experimentos realizados durante a atividade.

Foram discutidos:

- influência do tamanho da estrutura na quantidade de operações;
- diferença no crescimento do Bubble Sort e Quick Sort;
- importância de analisar operações e complexidade, além do resultado final.

📄 **[Acessar análise e conclusão](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-6-Analise-Conclusao/analise.md)**

---

# Atividade 3 - Análise de Algoritmos de Ordenação

Como complemento da atividade, foi desenvolvida uma análise prática comparando quatro algoritmos de ordenação:

- Bubble Sort;
- Insertion Sort;
- Selection Sort;
- Quick Sort.

Foram utilizados vetores com:

- 10 elementos;
- 20 elementos;
- 1.000 elementos.

Todos os algoritmos receberam cópias dos mesmos dados em cada experimento.

A quantidade de **comparações**, **trocas** e **movimentações** foi contabilizada para permitir uma comparação experimental entre os algoritmos.

📄 **[Acessar código da atividade prática](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Atividade-3-Ordenacao/ordenacao.py)**

📊 **[Acessar resultados e análise](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Atividade-3-Ordenacao/resultados.md)**

🧪 **[Acessar desafio – Organização inicial dos dados](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Atividade-3-Ordenacao/desafio.md)**

---

## Desafio - Influência da Organização Inicial dos Dados

No desafio da atividade prática, os algoritmos foram testados com **1.000 elementos** em três situações:

- vetor aleatório;
- vetor já ordenado;
- vetor em ordem inversa.

O objetivo foi observar se a organização inicial dos dados influencia a quantidade de operações realizadas.

Os resultados mostraram diferenças importantes entre os algoritmos.

No vetor aleatório, o **Quick Sort** apresentou o menor número de comparações.

No vetor já ordenado, o **Bubble Sort** e o **Insertion Sort** apresentaram apenas **999 comparações**.

No vetor inverso, Bubble Sort e Insertion Sort apresentaram uma quantidade muito elevada de operações.

O Quick Sort também apresentou um comportamento pior nas entradas ordenada e inversa devido à escolha do último elemento como pivô.

---

# Complexidade estudada

Durante a atividade foram trabalhadas diferentes formas de crescimento de algoritmos.

```text
O(1)       → Constante

O(n)       → Linear

O(n²)      → Quadrática

O(n log n) → Crescimento mais eficiente que O(n²)
```

Algumas das principais complexidades analisadas foram:

```text
Bubble Sort     → O(n²)
Insertion Sort  → O(n²)
Selection Sort  → O(n²)
Quick Sort      → O(n log n) em média
```

Um dos principais objetivos da atividade foi compreender que o aumento da quantidade de elementos pode alterar significativamente a quantidade de operações realizadas.

---

# Principais resultados observados

## Experimento com 1.000 elementos

Na execução mais recente da atividade prática, os resultados foram:

| Algoritmo | Comparações | Trocas/Movimentações | Total de operações |
|---|---:|---:|---:|
| Bubble Sort | 498.324 | 251.723 | 750.047 |
| Insertion Sort | 252.710 | 252.722 | 505.432 |
| Selection Sort | 499.500 | 994 | 500.494 |
| Quick Sort | 10.965 | 5.220 | 16.185 |

O **Quick Sort** apresentou a menor quantidade de operações contabilizadas nesse experimento.

---

## Busca sequencial em matrizes

Na busca sequencial em matrizes, foi observado que a posição do valor procurado influencia diretamente a quantidade de comparações.

Por exemplo:

```text
Matriz 100 × 100

Valor no início:
1 comparação

Valor próximo ao final:
9.999 comparações

Valor inexistente:
10.000 comparações
```

Esses resultados mostram, na prática, como o tamanho da estrutura e a posição dos elementos podem influenciar a quantidade de operações realizadas.

---

# Objetivo final

A atividade busca demonstrar que dois algoritmos podem produzir o mesmo resultado e, mesmo assim, apresentar custos computacionais diferentes.

Por isso, além de verificar se o algoritmo funciona corretamente, é importante analisar:

```text
Tamanho da entrada
        ↓
Quantidade de operações
        ↓
Complexidade
        ↓
Eficiência
```

---

## Tecnologias utilizadas

- Python
- Visual Studio Code
- Git
- GitHub

---

## Autor

**Pedro Henrique Silva Monteiro**

Projeto desenvolvido para fins acadêmicos na disciplina de **Estrutura de Dados II**.

