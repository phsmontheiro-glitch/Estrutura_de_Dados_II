# PARTE 5 - ANÁLISE DO MONITORAMENTO DE SENSORES

## Objetivo

Nesta parte da atividade foi desenvolvido um programa utilizando uma matriz para representar medições de temperatura realizadas por sensores.

O sistema possui:

```text
5 sensores
        ×
24 medições por sensor
        ↓
120 medições de temperatura
```

Cada linha da matriz representa um sensor e cada coluna representa um horário.

A estrutura utilizada pode ser representada da seguinte forma:

```text
sensores[sensor][horario]
```

Onde:

```text
Primeiro índice
[sensor]
        ↓
Representa o sensor


Segundo índice
[horario]
        ↓
Representa o horário da medição
```

---

# Estrutura da Matriz

O programa armazena as temperaturas em uma estrutura com:

```text
5 linhas
        ×
24 colunas
        ↓
120 posições
```

A representação pode ser entendida da seguinte forma:

```text
                Horários
        0    1    2    3   ...   23

Sensor 0   [ ]  [ ]  [ ]  [ ]  ...  [ ]

Sensor 1   [ ]  [ ]  [ ]  [ ]  ...  [ ]

Sensor 2   [ ]  [ ]  [ ]  [ ]  ...  [ ]

Sensor 3   [ ]  [ ]  [ ]  [ ]  ...  [ ]

Sensor 4   [ ]  [ ]  [ ]  [ ]  ...  [ ]
```

Cada posição da matriz armazena uma temperatura.

Por exemplo:

```text
sensores[2][10]
```

Representa:

```text
Sensor 2
        ↓
Temperatura registrada
        ↓
Horário 10
```

---

# Funcionamento do Programa

O programa realiza inicialmente a entrada das temperaturas.

Para isso, são utilizados loops aninhados.

O primeiro loop percorre os sensores:

```text
Sensor 0
Sensor 1
Sensor 2
Sensor 3
Sensor 4
```

Para cada sensor, um segundo loop percorre os horários:

```text
Horário 0
Horário 1
Horário 2
...
Horário 23
```

Portanto:

```text
5 sensores
        ×
24 horários
        ↓
120 temperaturas informadas
```

Cada temperatura é armazenada em uma posição correspondente da matriz.

---

# Análise das Temperaturas

Após receber as temperaturas, o programa percorre novamente a matriz para realizar diferentes análises.

Durante o mesmo percurso principal são realizadas várias operações.

---

## 1. Média de Cada Sensor

Para cada sensor, o programa soma suas 24 temperaturas.

Depois, a soma é dividida pela quantidade de medições realizadas por aquele sensor.

De forma simplificada:

```text
24 temperaturas
        ↓
Somar os valores
        ↓
Dividir por 24
        ↓
Média do sensor
```

Esse processo é realizado para todos os 5 sensores.

Portanto, ao final são obtidas:

```text
5 médias
```

Uma média para cada sensor.

---

## 2. Maior Temperatura Registrada

Durante o percurso da matriz, cada temperatura é comparada com a maior temperatura encontrada até aquele momento.

Inicialmente, o programa utiliza a primeira temperatura da matriz como referência:

```text
sensores[0][0]
```

Depois, cada nova temperatura é analisada.

Quando uma temperatura maior é encontrada:

```text
Temperatura atual
        >
Maior temperatura registrada
```

Os dados são atualizados.

O programa guarda:

- A maior temperatura;
- O sensor responsável;
- O horário da ocorrência.

Dessa forma, ao final do percurso, é possível saber não apenas qual foi a maior temperatura, mas também onde ela foi registrada.

---

## 3. Sensor Responsável Pela Maior Temperatura

Quando uma nova maior temperatura é encontrada, o programa armazena o índice do sensor.

Por exemplo:

```text
sensor_maior_temperatura = 3
```

Significa que:

```text
Sensor 3
```

Foi o responsável pela maior temperatura registrada até aquele momento.

Ao final do percurso, esse índice indica qual sensor registrou a maior temperatura presente em toda a matriz.

---

## 4. Horário da Ocorrência

Além do sensor, o programa também armazena o horário em que a maior temperatura ocorreu.

Por exemplo:

```text
horario_maior_temperatura = 15
```

Significa que a maior temperatura ocorreu no:

```text
Horário 15
```

O programa utiliza o segundo índice da matriz para identificar esse horário.

Portanto:

```text
sensores[sensor][horario]
```

Permite identificar:

```text
Qual sensor registrou
        +
Em qual horário ocorreu
```

---

## 5. Média Geral

Durante o percurso das temperaturas, todas as medições são somadas.

Como existem:

```text
5 sensores
        ×
24 medições
        ↓
120 medições
```

A média geral é calculada da seguinte forma:

```text
Soma de todas as temperaturas
        ↓
Divisão pela quantidade total de medições
        ↓
Média geral
```

No programa, a quantidade total de medições é calculada percorrendo os sensores e somando a quantidade de medições existentes em cada um.

O resultado esperado é:

```text
120 medições
```

---

## 6. Leituras Acima do Limite

O programa solicita ao usuário um limite de temperatura.

Por exemplo:

```text
Limite informado: 28°C
```

Durante o percurso da matriz, cada temperatura é comparada com esse limite.

Quando:

```text
Temperatura atual
        >
Limite informado
```

Um contador é incrementado.

Ao final, o programa informa quantas temperaturas ficaram acima do limite.

Essa análise permite verificar quantas medições ultrapassaram determinado valor.

---

# Por Que São Necessários Loops Aninhados?

Os loops aninhados são necessários porque os dados estão organizados em uma estrutura bidimensional.

A matriz possui:

```text
Linhas
        ↓
Sensores
```

E:

```text
Colunas
        ↓
Horários
```

Para acessar todas as posições, é necessário percorrer:

```text
Cada sensor
        ↓
Cada horário daquele sensor
        ↓
Cada temperatura armazenada
```

A estrutura dos loops pode ser representada da seguinte forma:

```text
Para cada sensor:

    Para cada horário:

        Acessar a temperatura
```

O primeiro loop controla qual sensor está sendo analisado.

O segundo loop percorre todas as medições daquele sensor.

Dessa forma, todas as posições da matriz podem ser acessadas.

---

# Papel dos Índices [i][j]

Os índices permitem localizar uma posição específica dentro da matriz.

De forma geral:

```text
sensores[i][j]
```

Onde:

```text
i
↓
Representa a linha
↓
Sensor


j
↓
Representa a coluna
↓
Horário
```

Por exemplo:

```text
sensores[4][23]
```

Representa:

```text
Sensor 4
        ↓
Medição realizada
        ↓
Horário 23
```

Os índices são importantes porque permitem identificar exatamente onde cada temperatura está armazenada.

Também permitem registrar a localização da maior temperatura encontrada.

---

# Quantidade de Posições Percorridas

A matriz possui:

```text
5 sensores
        ×
24 medições
        ↓
120 posições
```

Durante a análise principal dos sensores, todas as 120 posições precisam ser percorridas.

Portanto:

```text
5
×
24
=
120 acessos principais à matriz
```

Durante esse percurso, o programa realiza várias análises ao mesmo tempo.

Para cada temperatura, ele pode:

- Somar o valor para calcular a média do sensor;
- Somar o valor para calcular a média geral;
- Comparar com a maior temperatura;
- Comparar com o limite informado.

Isso é mais eficiente do que realizar um percurso completamente separado para cada análise.

---

# Relação Entre Linhas, Colunas e Quantidade de Operações

A quantidade total de posições de uma matriz depende da multiplicação entre o número de linhas e o número de colunas.

De forma geral:

```text
Número de linhas
        ×
Número de colunas
        ↓
Quantidade total de elementos
```

Neste experimento:

```text
5
×
24
=
120 elementos
```

Se o número de sensores ou horários aumentasse, a quantidade de posições também aumentaria.

Por exemplo:

```text
10 sensores
×
24 horários
=
240 medições
```

Ou:

```text
5 sensores
×
48 horários
=
240 medições
```

Portanto, o aumento das linhas ou das colunas aumenta a quantidade de elementos que precisam ser percorridos.

Essa relação pode ser representada como:

```text
Número de linhas
        ×
Número de colunas
        ↓
Quantidade de elementos
        ↓
Quantidade de acessos necessários
        ↓
Quantidade de operações
```

---

# Complexidade Computacional

Para analisar todas as temperaturas, o programa utiliza dois loops aninhados.

De forma geral:

```text
Para cada sensor:

    Para cada horário:

        Realizar operações
```

Se existirem:

```text
m sensores
```

E:

```text
n horários
```

A quantidade de posições que precisam ser percorridas é:

```text
m × n
```

Portanto, a complexidade do percurso principal é:

```text
O(m × n)
```

No caso específico desta atividade:

```text
5 × 24 = 120
```

Como todas as dimensões são percorridas, o algoritmo possui crescimento proporcional à quantidade de elementos existentes na matriz.

Mesmo realizando várias operações durante o mesmo percurso, como soma, comparação da maior temperatura e verificação do limite, a quantidade de operações por elemento permanece limitada por uma quantidade constante.

Portanto, o percurso principal continua apresentando complexidade:

```text
O(m × n)
```

---

# Análise da Quantidade de Operações

O programa realiza mais de uma etapa envolvendo percursos da estrutura.

As principais etapas são:

```text
Entrada das temperaturas:

5 × 24
=
120 posições
```

```text
Análise principal:

5 × 24
=
120 posições
```

```text
Exibição das temperaturas:

5 × 24
=
120 posições
```

Além disso, o programa percorre os sensores para calcular a quantidade total de medições:

```text
5 sensores
```

E percorre as médias dos sensores para exibi-las:

```text
5 médias
```

Portanto, considerando apenas os principais percursos:

```text
120
+
120
+
120
+
5
+
5
=
370 percursos aproximados
```

Essa quantidade representa uma estimativa dos principais acessos realizados às estruturas.

A quantidade exata de operações pode variar porque o programa também realiza:

- Comparações;
- Atribuições;
- Incrementos;
- Somatórios;
- Cálculos de divisão;
- Acessos aos índices.

Por esse motivo, a análise principal considera a quantidade de posições percorridas e não apenas cada instrução individual executada.

---

# Conclusão

O experimento permitiu aplicar os conceitos de matrizes, índices e loops aninhados em uma situação de monitoramento de sensores.

A matriz utilizada representa:

```text
5 sensores
        ×
24 horários
        ↓
120 medições
```

Cada linha representa um sensor e cada coluna representa um horário.

A utilização dos índices permite identificar exatamente onde uma temperatura está armazenada:

```text
sensores[sensor][horario]
```

Os loops aninhados permitem percorrer todas as posições da matriz e realizar diferentes análises.

Durante o percurso principal, o programa consegue:

- Calcular a média de cada sensor;
- Identificar a maior temperatura;
- Identificar o sensor responsável;
- Identificar o horário da ocorrência;
- Calcular a soma necessária para a média geral;
- Contar as temperaturas acima do limite informado.

A quantidade de operações necessárias está relacionada diretamente com o número de linhas e colunas da matriz.

Essa relação pode ser representada como:

```text
Número de sensores
        ×
Número de horários
        ↓
Quantidade de medições
        ↓
Quantidade de posições percorridas
        ↓
Quantidade de operações
```

De forma geral, para uma matriz com `m` linhas e `n` colunas, o percurso possui complexidade:

```text
O(m × n)
```

Dessa forma, a atividade demonstrou como matrizes e loops aninhados podem ser utilizados para armazenar e analisar grandes conjuntos de dados, além de mostrar que o aumento da quantidade de linhas e colunas influencia diretamente a quantidade de operações necessárias para processar todas as informações.

