# Atividade Avaliativa 2 - Estrutura de Dados II

## Sobre a atividade

Esta atividade foi desenvolvida para a disciplina de **Estrutura de Dados II**, com o objetivo de estudar e aplicar conceitos fundamentais de estruturas de dados, algoritmos de ordenação, busca, arrays, matrizes, loops e complexidade computacional.

Durante a atividade foram desenvolvidos códigos e experimentos para observar, medir e analisar a quantidade de operações realizadas pelos algoritmos.

---

## Conteúdos trabalhados

- Arrays
- Matrizes
- Índices
- Loops
- Loops aninhados
- Bubble Sort
- Quick Sort
- Busca sequencial
- Comparações
- Trocas e movimentações
- Complexidade computacional
- Análise experimental de algoritmos

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
└── Parte-6-Analise-Conclusao/
    └── analise.md
```

---

## Partes da atividade

### Parte 1 - Pesquisa

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

### Parte 2 - Experimento de Ordenação

Foi desenvolvido um experimento para comparar os algoritmos **Bubble Sort** e **Quick Sort** utilizando exatamente os mesmos dados.

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

### Parte 3 - Busca em Matrizes

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

### Parte 4 - Investigação do Array

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

### Parte 5 - Monitoramento de Sensores

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

### Parte 6 - Análise e Conclusão

Nesta etapa foram analisados os experimentos realizados durante a atividade.

Foram discutidos:

- influência do tamanho da estrutura na quantidade de operações;
- diferença no crescimento do Bubble Sort e Quick Sort;
- importância de analisar operações e complexidade, além do resultado final.

📄 **[Acessar análise e conclusão](https://github.com/phsmontheiro-glitch/Estrutura_de_Dados_II/blob/main/Atividade-Avaliativa-2/Parte-6-Analise-Conclusao/analise.md)**

---

## Complexidade estudada

Durante a atividade foram trabalhadas diferentes formas de crescimento de algoritmos.

```text
O(1)       → Constante

O(n)       → Linear

O(n²)      → Quadrática

O(n log n) → Crescimento mais eficiente que O(n²)
```

Um dos principais objetivos da atividade foi compreender que o aumento da quantidade de elementos pode alterar significativamente a quantidade de operações realizadas.

---

## Principais resultados observados

Nos experimentos de ordenação, a diferença entre os algoritmos se tornou mais evidente conforme o tamanho do array aumentou.

Com 1.000 elementos, por exemplo:

```text
Bubble Sort:

742.450 operações contabilizadas


Quick Sort:

15.526 operações contabilizadas
```

Na busca sequencial em matrizes, também foi observado que a posição do valor procurado influencia diretamente a quantidade de comparações.

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

## Objetivo final

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
