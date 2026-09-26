# ETAPA 02 --- Contrato Semântico e Testes


## Contrato semântico

O sistema recebe um tabuleiro de Sudoku clássico 9×9. Cada posição deve
conter um inteiro de `0` a `9`, sendo `0` a representação de uma posição
vazia.

O comportamento esperado é:

-   Se a entrada não possuir exatamente 9 linhas com 9 valores em cada
    linha, ou contiver valores fora do intervalo de 0 a 9, o resultado
    deverá ser **ENTRADA_INVÁLIDA**.
-   Se os valores fixos já violarem uma regra do Sudoku, o resultado
    deverá ser **TABULEIRO_INVÁLIDO**.
-   Se o tabuleiro estiver completo e válido, o resultado deverá ser
    **JÁ_RESOLVIDO**, preservando o tabuleiro.
-   Se o tabuleiro estiver incompleto e puder ser resolvido, o resultado
    deverá ser **SOLUCIONADO**, acompanhado de um tabuleiro completo que
    preserve todos os valores fixos e respeite as regras do Sudoku.
-   Se o tabuleiro for inicialmente válido, mas não existir
    preenchimento completo que satisfaça todas as regras, o resultado
    deverá ser **SEM_SOLUÇÃO**.
-   Quando houver mais de uma solução possível, qualquer solução
    completa e válida que preserve os valores fixos será aceita.


## Casos normais

### CN-01 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-02 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
0 3 4 6 7 8 9 1 2
6 0 2 1 9 5 3 4 8
1 9 0 3 4 2 5 6 7
8 5 9 0 6 1 4 2 3
4 2 6 8 0 3 7 9 1
7 1 3 9 2 0 8 5 6
9 6 1 5 3 7 0 8 4
2 8 7 4 1 9 6 0 5
3 4 5 2 8 6 1 7 0
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-03 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
5 0 4 6 0 8 9 0 2
0 7 2 0 9 5 0 4 8
1 9 0 3 4 0 5 6 0
8 0 9 7 0 1 4 0 3
0 2 6 0 5 3 0 9 1
7 1 0 9 2 0 8 5 0
9 0 1 5 0 7 2 0 4
0 8 7 0 1 9 0 3 5
3 4 0 2 8 0 1 7 0
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-04 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
0 0 4 6 7 8 9 1 2
6 7 0 0 9 5 3 4 8
1 9 8 3 0 0 5 6 7
8 5 9 7 6 1 0 0 3
0 2 6 8 5 3 7 9 0
7 0 0 9 2 4 8 5 6
9 6 1 0 0 7 2 8 4
2 8 7 4 1 0 0 3 5
3 4 5 2 8 6 1 0 0
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-05 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
5 3 4 0 0 0 9 1 2
6 7 2 0 0 0 3 4 8
1 9 8 0 0 0 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-06 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
5 3 4 6 7 8 9 1 2
0 0 0 0 0 0 0 0 0
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
0 0 0 0 0 0 0 0 0
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
0 0 0 0 0 0 0 0 0
3 4 5 2 8 6 1 7 9
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-07 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
0 0 0 6 7 8 9 1 2
0 0 0 1 9 5 3 4 8
0 0 0 3 4 2 5 6 7
8 5 9 0 0 0 4 2 3
4 2 6 0 0 0 7 9 1
7 1 3 0 0 0 8 5 6
9 6 1 5 3 7 0 0 0
2 8 7 4 1 9 0 0 0
3 4 5 2 8 6 0 0 0
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-08 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
5 0 0 6 0 0 9 0 0
0 7 0 0 9 0 0 4 0
0 0 8 0 0 2 0 0 7
8 0 0 7 0 0 4 0 0
0 2 0 0 5 0 0 9 0
0 0 3 0 0 4 0 0 6
9 0 0 5 0 0 2 0 0
0 8 0 0 1 0 0 3 0
0 0 5 0 0 6 0 0 9
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-09 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
0 3 0 6 0 8 0 1 0
6 0 2 0 9 0 3 0 8
0 9 0 3 0 2 0 6 0
8 0 9 0 6 0 4 0 3
0 2 0 8 0 3 0 9 0
7 0 3 0 2 0 8 0 6
0 6 0 5 0 7 0 8 0
2 0 7 0 1 0 6 0 5
0 4 0 2 0 6 0 7 0
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CN-10 --- Sudoku incompleto válido

**Descrição:** Verifica a resolução de um tabuleiro 9×9 válido com
posições vazias.

**Entrada:**

``` text
5 3 4 6 7 8 9 1 0
6 7 2 1 9 5 3 0 8
1 9 8 3 4 2 0 6 7
8 5 9 7 6 0 4 2 3
4 2 6 8 0 3 7 9 1
7 1 3 0 2 4 8 5 6
9 6 0 5 3 7 2 8 4
2 0 7 4 1 9 6 3 5
0 4 5 2 8 6 1 7 9
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## Casos-limite

### CL-01 --- Apenas uma posição vazia

**Descrição:** Verifica o comportamento quando falta apenas um valor
para completar o Sudoku.

**Entrada:**

``` text
5 3 4 6 7 8 9 1 0
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

**Saída esperada:** `SOLUCIONADO`

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

### CL-02 --- Tabuleiro já completo e válido

**Descrição:** Verifica se um Sudoku que já está resolvido é reconhecido
sem alteração.

**Entrada:**

``` text
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

**Saída esperada:** `JÁ_RESOLVIDO`, mantendo exatamente o mesmo
tabuleiro.

### CL-03 --- Tabuleiro completamente vazio

**Descrição:** Verifica o limite em que nenhuma posição inicial está
preenchida. Existem múltiplas soluções possíveis.

**Entrada:**

``` text
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```

**Saída esperada:** `SOLUCIONADO`, acompanhado de qualquer tabuleiro 9×9
completo que respeite todas as regras do Sudoku.

## Casos de entrada inválida

### CI-01 --- Quantidade incorreta de linhas

**Descrição:** Verifica a rejeição de uma entrada que não possui as
dimensões 9×9.

**Entrada:**

``` text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
```

**Saída esperada:** `ENTRADA_INVÁLIDA`.

### CI-02 --- Valor fora do intervalo permitido

**Descrição:** Verifica a rejeição de um tabuleiro 9×9 que contém um
valor diferente de 0 a 9.

**Entrada:**

``` text
5 3 0 0 7 0 0 0 10
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

**Saída esperada:** `ENTRADA_INVÁLIDA`.

## Observação para as próximas etapas

Estes casos formam o contrato de comportamento do projeto. As
implementações imperativa, orientada a objetos, funcional e lógica
deverão, sempre que aplicável, ser avaliadas com os mesmos casos,
independentemente de como cada solução for construída.
