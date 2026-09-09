# [P4-ETAPA-01]

## Sistema de Resolução e Validação de Sudoku

### 1. Descrição do problema

O Sudoku é um quebra-cabeça lógico composto por uma grade de 9 linhas e 9 colunas, totalizando 81 posições. A grade também é dividida em nove regiões de tamanho 3×3.

No início do problema, algumas posições já possuem valores entre 1 e 9, enquanto as demais estão vazias. O desafio consiste em preencher todas as posições vazias respeitando as regras do Sudoku.

O problema escolhido para este projeto consiste em desenvolver um sistema capaz de receber um tabuleiro de Sudoku, verificar sua validade e, caso esteja incompleto e possua solução, determinar valores para as posições vazias de maneira que todas as regras do jogo sejam satisfeitas.

O sistema também deverá ser capaz de identificar situações nas quais o tabuleiro fornecido já é inválido ou não possui uma solução possível.

---

### 2. Objetivo

O objetivo do sistema é resolver e validar tabuleiros de Sudoku clássico 9×9.

A partir de um tabuleiro informado, o sistema deverá ser capaz de:

* verificar se os valores inicialmente preenchidos respeitam as regras do Sudoku;
* identificar as posições que ainda precisam ser preenchidas;
* encontrar uma solução válida para o tabuleiro, quando ela existir;
* apresentar o tabuleiro completo após a resolução;
* identificar quando um tabuleiro não pode ser resolvido devido a contradições;
* reconhecer quando um tabuleiro já está completamente preenchido e válido.

---

### 3. Entradas

A entrada do sistema será um tabuleiro de Sudoku composto por 9 linhas e 9 colunas.

Cada posição poderá conter:

* um número inteiro entre 1 e 9, representando uma posição já preenchida;
* um valor convencionado para representar uma posição vazia, como 0.

Exemplo de entrada:

```text
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

Nesse formato, o valor `0` representa uma posição que ainda deve ser preenchida.

---

### 4. Saídas

Quando o Sudoku possuir solução, o sistema deverá apresentar o tabuleiro completamente preenchido e válido.

Exemplo:

```text
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

Quando o tabuleiro não for válido ou não possuir solução, o sistema deverá informar essa condição em vez de apresentar uma solução incorreta.

Caso o tabuleiro recebido já esteja completo e seja válido, o próprio tabuleiro poderá ser apresentado como resultado, acompanhado da indicação de que ele já estava resolvido.

---

### 5. Regras do problema

O comportamento do sistema deverá obedecer às seguintes regras:

1. O tabuleiro deve possuir exatamente 9 linhas e 9 colunas.

2. Cada posição preenchida deve conter um número inteiro entre 1 e 9.

3. Posições vazias devem ser representadas pelo valor definido para ausência de número.

4. Cada linha do tabuleiro deve conter os números de 1 a 9 sem repetição quando estiver completamente preenchida.

5. Uma linha não pode possuir dois valores preenchidos iguais.

6. Cada coluna deve conter os números de 1 a 9 sem repetição quando estiver completamente preenchida.

7. Uma coluna não pode possuir dois valores preenchidos iguais.

8. Cada uma das nove regiões 3×3 deve conter os números de 1 a 9 sem repetição quando estiver completamente preenchida.

9. Uma região 3×3 não pode possuir dois valores preenchidos iguais.

10. Os números presentes no tabuleiro de entrada são considerados fixos e não podem ser alterados durante a resolução.

11. Um número somente pode ser colocado em uma posição vazia quando sua presença não violar nenhuma regra de linha, coluna ou região 3×3.

12. Uma solução somente será considerada válida quando todas as 81 posições estiverem preenchidas e todas as regras do Sudoku forem satisfeitas.

13. Caso não exista nenhuma forma de preencher todas as posições sem violar as regras, o sistema deverá indicar que o Sudoku não possui solução.

14. Caso o tabuleiro inicial já viole alguma regra do Sudoku, ele deverá ser identificado como inválido.

---

### 6. Casos de exemplo

#### Exemplo 1 — Sudoku incompleto válido

**Entrada:**

```text
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

**Saída esperada:**

```text
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

#### Exemplo 2 — Sudoku já resolvido

**Entrada:** um tabuleiro 9×9 completamente preenchido e que respeita todas as regras.

**Saída esperada:**

```text
O Sudoku já está resolvido e é válido.
```

O tabuleiro recebido permanece inalterado.

#### Exemplo 3 — Valor repetido em uma linha

**Entrada:** um tabuleiro contendo, por exemplo, dois números `5` já preenchidos na mesma linha.

**Saída esperada:**

```text
Tabuleiro inválido: existe valor repetido em uma linha.
```

#### Exemplo 4 — Valor repetido em uma coluna

**Entrada:** um tabuleiro contendo dois valores iguais já preenchidos na mesma coluna.

**Saída esperada:**

```text
Tabuleiro inválido: existe valor repetido em uma coluna.
```

#### Exemplo 5 — Sudoku válido inicialmente, mas sem solução

**Entrada:** um tabuleiro que não apresenta repetição imediata entre seus valores preenchidos, mas cujas restrições tornam impossível completar todas as posições.

**Saída esperada:**

```text
O Sudoku não possui solução.
```

---

### 7. Casos-limite

**Tabuleiro completamente vazio:**
Todas as 81 posições estão vazias. O tabuleiro não viola inicialmente as regras do Sudoku e existem diversas soluções possíveis. O sistema deverá ser capaz de apresentar uma solução válida.

**Tabuleiro completamente preenchido:**
Caso todas as posições estejam preenchidas, o sistema deverá apenas verificar as regras. Se todas forem satisfeitas, o tabuleiro será considerado resolvido. Caso exista alguma violação, será considerado inválido.

**Tabuleiro sem solução:**
Pode existir um tabuleiro que não apresente uma violação evidente em sua configuração inicial, mas para o qual nenhuma combinação possível complete todas as posições. Nesse caso, o sistema deverá informar que não existe solução.

**Entrada fora das dimensões esperadas:**
Caso o tabuleiro possua quantidade diferente de 9 linhas ou 9 colunas, a entrada deverá ser considerada inválida.

---

### 8. Restrições

O projeto será limitado ao Sudoku clássico de tamanho 9×9, dividido em nove regiões 3×3.

Não fazem parte do escopo:

* outras variações de tamanho, como Sudoku 4×4 ou 16×16;
* variantes com regras adicionais, como Killer Sudoku, Samurai Sudoku ou Sudoku diagonal;
* geração automática de novos quebra-cabeças;
* avaliação do nível de dificuldade de um Sudoku;
* sistema de dicas para jogadores;
* interface gráfica;
* reconhecimento de Sudoku por fotografias ou imagens;
* competição entre jogadores ou controle de pontuação.

O foco será exclusivamente na validação e resolução de tabuleiros de Sudoku clássico.

---

### 9. Principais conceitos do domínio

Os principais conceitos envolvidos no problema são:

**Tabuleiro:** conjunto das 81 posições que formam o Sudoku.

**Posição:** local específico do tabuleiro, identificado por sua linha e coluna, que pode estar preenchido ou vazio.

**Linha:** conjunto horizontal formado por nove posições.

**Coluna:** conjunto vertical formado por nove posições.

**Região:** conjunto de nove posições pertencentes a uma das nove áreas 3×3 do tabuleiro.

**Valor:** número inteiro entre 1 e 9 que pode ocupar uma posição.

**Posição fixa:** posição cujo valor foi fornecido no tabuleiro inicial e não pode ser modificado.

**Solução:** preenchimento completo das posições vazias que satisfaz simultaneamente todas as regras do Sudoku.

**Restrição:** condição que determina quais valores podem ou não ocupar determinada posição.

---

### 10. Adequação aos quatro paradigmas

O problema de resolução de Sudoku pode ser abordado utilizando os quatro paradigmas estudados na disciplina.

**Paradigma imperativo:**
O problema pode ser descrito como uma sequência de operações sobre o estado do tabuleiro, verificando posições e valores até que uma solução seja encontrada.

**Paradigma orientado a objetos:**
Os diferentes conceitos existentes no domínio do Sudoku, como tabuleiro, posições e regras, permitem organizar o problema a partir de entidades que possuem características e responsabilidades relacionadas à resolução e validação.

**Paradigma funcional:**
O processo pode ser representado por funções que recebem estados do tabuleiro e produzem novos estados ou resultados, permitindo expressar validações e transformações sem depender necessariamente de alterações diretas no estado original.

**Paradigma lógico:**
O Sudoku é naturalmente definido por um conjunto de fatos, relações e restrições. A solução pode ser caracterizada como uma atribuição de valores às posições que satisfaça simultaneamente todas as regras de linhas, colunas e regiões.

Dessa forma, o mesmo problema permite diferentes formas de modelagem e resolução, sendo adequado para comparar as características dos quatro paradigmas.

---

### 11. Linguagens inicialmente consideradas

Como linguagem principal, inicialmente será considerada **Python**, pois permite trabalhar com diferentes estilos e paradigmas de programação e possui uma sintaxe relativamente simples.

Para o paradigma **imperativo**, Python pode representar diretamente sequências de operações, decisões e repetições necessárias para manipular e verificar o tabuleiro.

Para o paradigma **orientado a objetos**, Python oferece suporte a conceitos como classes, objetos, encapsulamento e composição.

Para o paradigma **funcional**, Python possui suporte a funções como valores, funções de ordem superior e outras construções que permitem desenvolver uma solução com características funcionais.

Para o paradigma **lógico**, inicialmente será considerada a possibilidade de utilizar recursos ou bibliotecas de programação lógica disponíveis para Python. Como alternativa, caso seja necessário utilizar uma linguagem especificamente voltada ao paradigma lógico, poderá ser considerado o **Prolog**, por permitir representar naturalmente fatos, relações, regras e consultas.

A escolha definitiva das ferramentas para cada paradigma poderá ser realizada nas etapas de implementação, mantendo o problema especificado nesta etapa independente de uma linguagem específica.
