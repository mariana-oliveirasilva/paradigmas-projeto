# Etapa 03 — Implementação Imperativa

## Problema

Esta implementação resolve e valida Sudoku clássico 9×9 conforme a especificação da Etapa 01 e o contrato semântico definido na Etapa 02. O valor `0` representa uma posição vazia.

## Decisões de implementação

### Estados mantidos

O principal estado mantido pelo programa é o próprio tabuleiro, representado por uma matriz 9×9 de números inteiros. Durante a resolução, as posições inicialmente vazias passam temporariamente a armazenar valores entre 1 e 9.

Além do tabuleiro, o fluxo utiliza variáveis locais como linha, coluna, número testado e limites da região 3×3. Essas variáveis representam o estado momentâneo de cada subprograma.

### Operações que modificam estado

A principal modificação de estado ocorre em `resolver`. Quando um número pode ocupar uma posição, ele é atribuído diretamente à matriz:

```python
tabuleiro[linha][coluna] = numero
```

Se essa escolha impedir a conclusão do Sudoku, a tentativa é desfeita:

```python
tabuleiro[linha][coluna] = 0
```

Esse processo de tentativa, alteração e restauração do estado continua até uma solução ser encontrada ou até que todas as possibilidades sejam esgotadas.

### Efeitos colaterais

`resolver` possui como efeito colateral a alteração do tabuleiro recebido por parâmetro. Quando encontra uma solução, a matriz original permanece preenchida com a solução encontrada.

`imprimir_tabuleiro` também possui efeito colateral, pois produz saída no terminal. As funções de validação apenas consultam os dados e retornam resultados.

### Estruturas de controle utilizadas

A implementação utiliza:

- `for` para percorrer linhas, colunas, regiões e números candidatos;
- `if` para decisões e validações;
- retornos antecipados para interromper verificações quando uma condição já determina o resultado;
- chamadas recursivas em `resolver` para continuar a busca a partir do estado atual;
- atribuições para modificar explicitamente o estado do tabuleiro durante a resolução.

A recursão é utilizada como parte do processo de backtracking, mas o estado continua sendo alterado explicitamente na mesma matriz, preservando a natureza imperativa da solução.

### Organização dos subprogramas

A solução foi dividida nos seguintes subprogramas:

- `entrada_valida`: verifica formato, dimensões e valores da entrada;
- `numero_valido`: verifica se um número respeita linha, coluna e região 3×3;
- `tabuleiro_inicial_valido`: verifica se os valores fixos já violam alguma regra;
- `encontrar_vazio`: localiza a próxima posição ainda não preenchida;
- `resolver`: modifica o tabuleiro até encontrar uma solução, usando backtracking;
- `tabuleiro_completo`: verifica se ainda existem posições vazias;
- `processar_sudoku`: controla o fluxo principal do contrato semântico;
- `imprimir_tabuleiro`: apresenta o tabuleiro no terminal;
- `main`: fornece um ponto de entrada e um exemplo de execução.

Os parâmetros permitem que cada subprograma receba apenas as informações necessárias para executar sua responsabilidade.

## Por que a solução é predominantemente imperativa

A solução é predominantemente imperativa porque descreve explicitamente uma sequência de operações que modificam o estado do programa. O tabuleiro é percorrido por estruturas de repetição e tem suas posições alteradas por atribuições durante a busca da solução.

O fluxo de execução é determinado por laços, condicionais, chamadas de subprogramas e alterações diretas da matriz. Não são utilizadas classes ou objetos para esconder essas mudanças de estado.

## Validação

A implementação deve ser validada com os mesmos casos definidos em `testes/casos.md` na Etapa 02. O contrato considera os resultados semânticos:

- `SOLUCIONADO`;
- `JA_RESOLVIDO`;
- `TABULEIRO_INVALIDO`;
- `SEM_SOLUCAO`;
- `ENTRADA_INVALIDA`.

Quando o resultado for `SOLUCIONADO`, o tabuleiro alterado deverá estar completo, preservar os valores fixos da entrada e respeitar as regras de linhas, colunas e regiões 3×3.

## Execução

Na raiz do repositório, execute:

```bash
python imperativo/sudoku.py
```

O exemplo presente em `main` pode ser substituído pelos casos definidos na Etapa 02.
