# PARTE 1 – PESQUISA: BUBBLE SORT E QUICK SORT

## Objetivo

Nesta primeira parte da atividade será realizada uma pesquisa sobre os algoritmos de ordenação **Bubble Sort** e **Quick Sort**.

Serão analisados o funcionamento, a lógica de ordenação, as complexidades computacionais, as vantagens, limitações e situações em que cada algoritmo pode ser utilizado.

---

# 1. BUBBLE SORT

## Como o algoritmo funciona

O Bubble Sort é um algoritmo de ordenação baseado na comparação entre elementos vizinhos de um array.

O algoritmo percorre o array comparando dois elementos por vez. Quando os elementos estão na ordem errada, eles trocam de posição.

Esse processo é repetido até que todos os elementos estejam organizados.

O nome Bubble Sort, ou ordenação por bolha, vem da ideia de que os maiores valores parecem "subir" até o final do array durante as passagens.

## Lógica de ordenação

A lógica do Bubble Sort funciona da seguinte forma:

1. Percorrer o array;
2. Comparar um elemento com o seu vizinho;
3. Verificar se o primeiro elemento é maior que o próximo;
4. Caso esteja na ordem errada, realizar uma troca;
5. Continuar comparando os elementos vizinhos;
6. Repetir o processo até que o array esteja ordenado.

### Exemplo

Array inicial:

```text
7, 3, 5
```

Primeira comparação:

```text
7 > 3
```

Como `7` é maior que `3`, ocorre uma troca:

```text
3, 7, 5
```

Próxima comparação:

```text
7 > 5
```

Como `7` é maior que `5`, ocorre outra troca:

```text
3, 5, 7
```

Após as comparações, o array fica ordenado.

## Complexidade no melhor caso

`O(n)`

O melhor caso acontece quando o array já está ordenado e o algoritmo possui uma verificação para perceber que nenhuma troca foi realizada.

Nesse caso, é necessário apenas percorrer o array uma vez para verificar que ele já está organizado.

## Complexidade no caso médio

`O(n²)`

No caso médio, o algoritmo precisa realizar diversas comparações e possíveis trocas para organizar os elementos.

À medida que o número de elementos aumenta, a quantidade de operações cresce de forma quadrática.

## Complexidade no pior caso

`O(n²)`

O pior caso acontece quando o array está organizado na ordem contrária à desejada.

Por exemplo:

```text
5, 4, 3, 2, 1
```

Nesse caso, serão necessárias muitas comparações e trocas para organizar todos os elementos.

## Vantagens

* Fácil de entender;
* Fácil de implementar;
* Possui uma lógica simples;
* É útil para aprender conceitos de ordenação;
* Ajuda a compreender comparações e trocas entre elementos.

## Limitações

* Não possui boa eficiência para grandes quantidades de dados;
* Pode realizar muitas comparações;
* Pode realizar muitas trocas;
* Possui complexidade `O(n²)` no caso médio e no pior caso;
* O crescimento da quantidade de operações é elevado quando o tamanho do array aumenta.

## Situações em que seu uso é adequado

O Bubble Sort pode ser adequado:

* Para fins educacionais;
* Para aprender algoritmos de ordenação;
* Para arrays pequenos;
* Para compreender comparações, índices e trocas;
* Para situações simples onde o desempenho não é importante.

## Situações em que seu uso não é recomendado

O Bubble Sort não é recomendado:

* Para grandes quantidades de dados;
* Para sistemas onde o desempenho é importante;
* Quando é necessário ordenar muitos elementos rapidamente;
* Quando existem algoritmos mais eficientes disponíveis.

---

# 2. QUICK SORT

## Como o algoritmo funciona

O Quick Sort é um algoritmo de ordenação que utiliza a estratégia de dividir um problema maior em problemas menores.

O algoritmo escolhe um elemento chamado **pivô**.

Depois, os outros elementos são organizados em relação a esse pivô:

* Elementos menores ficam de um lado;
* Elementos maiores ficam do outro lado.

Após essa divisão, o mesmo processo é repetido nas partes menores até que todo o array esteja ordenado.

## Lógica de ordenação

A lógica do Quick Sort consiste em:

1. Escolher um pivô;
2. Comparar os elementos com o pivô;
3. Separar os elementos menores e maiores;
4. Colocar o pivô em sua posição correta;
5. Repetir o processo nas partes menores;
6. Continuar até que todas as partes estejam ordenadas.

O Quick Sort utiliza uma estratégia conhecida como **dividir e conquistar**, pois divide um problema maior em problemas menores.

## Exemplo

Array inicial:

```text
7, 3, 5
```

Supondo que o pivô escolhido seja:

```text
3
```

Os elementos são analisados em relação ao pivô:

```text
Menores que 3: nenhum

Pivô: 3

Maiores que 3: 7, 5
```

Depois, o processo continua na parte:

```text
7, 5
```

Após as comparações e organização:

```text
3, 5, 7
```

O processo continua até que todas as partes estejam ordenadas.

## Complexidade no melhor caso

`O(n log n)`

O melhor caso acontece quando o pivô consegue dividir o array em partes relativamente equilibradas.

Por exemplo:

```text
8 elementos
↓
divide em aproximadamente 4 e 4
↓
depois divide novamente
↓
continua até organizar
```

Essa divisão equilibrada reduz a quantidade de operações necessárias.

## Complexidade no caso médio

`O(n log n)`

No caso médio, o Quick Sort apresenta uma boa eficiência.

Por esse motivo, geralmente é muito mais eficiente que o Bubble Sort quando o número de elementos aumenta.

## Complexidade no pior caso

`O(n²)`

O pior caso pode acontecer quando o pivô é escolhido de uma forma que gera divisões muito desequilibradas.

Por exemplo, quando um lado fica praticamente vazio e o outro continua contendo quase todos os elementos.

Nesse caso, o comportamento do algoritmo pode se aproximar de uma ordenação quadrática.

## Vantagens

* Geralmente é mais eficiente que o Bubble Sort;
* Possui complexidade `O(n log n)` no melhor caso;
* Possui complexidade `O(n log n)` no caso médio;
* É adequado para grandes quantidades de dados;
* Utiliza a estratégia de dividir o problema em partes menores.

## Limitações

* É mais complexo de entender e implementar;
* A escolha do pivô influencia o desempenho;
* Pode apresentar complexidade `O(n²)` no pior caso;
* Implementações tradicionais utilizam recursão.

## Situações em que seu uso é adequado

O Quick Sort é recomendado:

* Para grandes arrays;
* Para ordenar grandes quantidades de dados;
* Quando o desempenho é importante;
* Quando se deseja um algoritmo eficiente no caso médio;
* Em situações onde uma boa estratégia para escolher o pivô pode ser utilizada.

## Situações em que seu uso não é recomendado

O Quick Sort pode não ser a melhor opção:

* Quando é necessário garantir `O(n log n)` no pior caso;
* Quando a implementação recursiva pode causar problemas de memória;
* Em situações muito simples onde um algoritmo básico já é suficiente.

---

# 3. TABELA COMPARATIVA

| Característica             | Bubble Sort                                                   | Quick Sort                                                         |
| -------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------ |
| Princípio de funcionamento | Compara elementos vizinhos e realiza trocas quando necessário | Escolhe um pivô e divide os elementos em menores e maiores que ele |
| Melhor caso                | `O(n)`                                                        | `O(n log n)`                                                       |
| Caso médio                 | `O(n²)`                                                       | `O(n log n)`                                                       |
| Pior caso                  | `O(n²)`                                                       | `O(n²)`                                                            |
| Uso de memória             | Baixo, geralmente `O(1)`                                      | Utiliza memória adicional devido às chamadas recursivas            |
| Vantagem principal         | Simples e fácil de entender                                   | Geralmente é mais eficiente para grandes quantidades de dados      |
| Limitação principal        | Ineficiente para grandes arrays                               | O desempenho pode ser prejudicado por uma escolha ruim do pivô     |
| Aplicação recomendada      | Aprendizado e arrays pequenos                                 | Arrays maiores e situações que exigem maior eficiência             |

---

# 4. COMPARAÇÃO ENTRE OS ALGORITMOS

Os dois algoritmos possuem o mesmo objetivo: organizar os elementos de uma estrutura de dados.

Entretanto, eles utilizam estratégias diferentes.

O Bubble Sort compara elementos vizinhos e realiza trocas quando necessário.

O Quick Sort escolhe um pivô e divide o problema em partes menores.

Essa diferença influencia diretamente a quantidade de operações realizadas.

Para arrays pequenos, a diferença pode não ser tão perceptível.

Porém, à medida que o número de elementos aumenta, o Bubble Sort tende a realizar uma quantidade muito maior de comparações e trocas devido à sua complexidade quadrática.

O Quick Sort, quando apresenta divisões equilibradas, possui um crescimento menor de operações devido à sua complexidade média `O(n log n)`.

---

# 5. CONCLUSÃO DA PESQUISA

Os algoritmos Bubble Sort e Quick Sort podem produzir exatamente o mesmo resultado final, ou seja, um array ordenado.

Porém, a quantidade de operações necessárias para chegar ao resultado pode ser completamente diferente.

O Bubble Sort possui uma lógica simples baseada em comparações entre elementos vizinhos. Essa simplicidade facilita o aprendizado, mas pode causar uma grande quantidade de operações quando o número de elementos aumenta.

O Quick Sort utiliza uma estratégia baseada na escolha de um pivô e na divisão do problema em partes menores. No caso médio, essa estratégia permite uma maior eficiência.

Portanto, não é suficiente analisar apenas o resultado final de um algoritmo.

Também é importante analisar:

```text
Tamanho da entrada
        ↓
Quantidade de operações
        ↓
Complexidade computacional
        ↓
Eficiência do algoritmo
```

Nas próximas partes da atividade, os algoritmos serão testados experimentalmente utilizando arrays de diferentes tamanhos, permitindo comparar a quantidade de comparações e movimentações realizadas por cada um.
