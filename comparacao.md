# ETAPA 05 --- COMPARAÇÃO ENTRE IMPERATIVO E POO

Projeto: Sistema de Resolução e Validação de Sudoku 9×9

Tag de entrega: P4-ETAPA-05

## 1. Introdução

Esta etapa compara as duas implementações já produzidas para o mesmo
problema: um solucionador e validador de Sudoku 9×9. A primeira
implementação foi estruturada de forma predominantemente imperativa,
enquanto a segunda foi remodelada segundo orientação a objetos. As duas
preservam o mesmo objetivo e utilizam o algoritmo de backtracking para
encontrar uma solução, mas organizam estado, responsabilidades e
operações de maneiras diferentes.

A comparação abaixo é baseada diretamente no código produzido nas Etapas
03 e 04. Na versão imperativa, o tabuleiro é uma lista de listas
manipulada por funções como entrada_valida, numero_valido,
encontrar_vazio, resolver e processar_sudoku. Na versão orientada a
objetos, o sistema foi dividido principalmente entre TabuleiroSudoku,
ValidadorSudoku, SolucionadorSudoku, SolucionadorBacktracking,
ResultadoSudoku e AplicacaoSudoku.

## 2. Análise comparativa

### 2.1 Representação do estado

Na implementação imperativa, o estado principal é a própria matriz
tabuleiro, representada por uma lista de listas. Ela é recebida como
parâmetro pelas funções e pode ser modificada diretamente, como ocorre
em `tabuleiro[linha][coluna] = numero` durante a resolução.

Na implementação orientada a objetos, o estado do Sudoku fica
concentrado no objeto TabuleiroSudoku, no atributo `self.`\_valores\`\`.
O restante do sistema trabalha com esse objeto por meio de métodos como
obter, definir, encontrar_vazio, valores_da_linha e valores_da_coluna.
Além disso, o construtor faz uma cópia defensiva da lista recebida,
evitando que o estado interno seja simplesmente a mesma lista externa
fornecida pelo chamador.

### 2.2 Mutabilidade

As duas implementações são mutáveis durante o backtracking. Na versão
imperativa, a alteração é explícita na matriz:
`tabuleiro[linha][coluna] = numero` e, quando a tentativa falha,
`tabuleiro[linha][coluna] = 0`.

Na versão POO, a mesma ideia continua existindo, mas a mutação é feita
através de `tabuleiro.definir(linha, coluna, valor)`. Se a tentativa
falha, o solucionador chama
`tabuleiro.definir(linha, coluna, TabuleiroSudoku.VAZIO)`. Assim, a
mutabilidade não desapareceu; ela foi encapsulada pelo objeto.

### 2.3 Fluxo de controle

Na versão imperativa, o fluxo é muito direto. A função processar_sudoku
chama as validações em sequência e depois chama resolver. Dentro de
resolver, há um for de 1 a 9, uma verificação com numero_valido e uma
chamada recursiva.

Na versão POO, o fluxo lógico é semelhante, mas passa pela colaboração
entre objetos. AplicacaoSudoku.executar coordena ValidadorSudoku e
SolucionadorSudoku. O SolucionadorBacktracking, por sua vez, utiliza o
validador e o TabuleiroSudoku. Portanto, o fluxo está mais distribuído
entre componentes.

### 2.4 Decomposição do problema

No imperativo, a decomposição ocorre principalmente por funções. Cada
função possui uma tarefa específica: validar a entrada, verificar um
número, validar o tabuleiro inicial, encontrar uma casa vazia, resolver,
verificar se está completo e imprimir.

Na POO, a decomposição é feita principalmente por responsabilidades de
classes. TabuleiroSudoku representa e controla o estado; ValidadorSudoku
concentra regras de validade; SolucionadorSudoku define a abstração de
resolução; SolucionadorBacktracking implementa a estratégia; e
AplicacaoSudoku coordena o caso de uso.

### 2.5 Reutilização

As funções imperativas podem ser reutilizadas isoladamente, por exemplo
numero_valido e encontrar_vazio. Porém, a versão POO cria pontos de
reutilização mais estruturados. AplicacaoSudoku depende da abstração
SolucionadorSudoku, o que permite utilizar outra implementação de
solucionador sem alterar a classe coordenadora. ValidadorSudoku também
pode ser compartilhado com diferentes estratégias de resolução.

### 2.6 Manutenção

A versão imperativa é menor e direta, o que facilita compreender
rapidamente um programa desse tamanho. Por outro lado, funções
diferentes recebem e manipulam a mesma estrutura de dados diretamente.

Na POO, as responsabilidades estão mais separadas. Uma mudança na
representação interna do tabuleiro tende a ficar concentrada em
TabuleiroSudoku; uma mudança nas regras de validação fica principalmente
em ValidadorSudoku; e mudanças na estratégia de resolução ficam no
solucionador. Isso reduz o acoplamento conceitual entre
responsabilidades, embora aumente a quantidade de código.

### 2.7 Facilidade de extensão

A POO oferece uma vantagem clara quando se pensa em novas estratégias de
resolução. Como SolucionadorSudoku é uma classe abstrata e
AplicacaoSudoku recebe um objeto desse tipo, seria possível criar outro
solucionador que implementasse o mesmo método resolver e substituí-lo na
aplicação. Na versão imperativa, essa troca exigiria reorganizar
chamadas de funções ou criar manualmente uma nova função e adaptar o
fluxo que a utiliza.

### 2.8 Tratamento de erros

Na versão imperativa, entradas inadequadas são tratadas principalmente
por verificações e retornos booleanos ou estados textuais, como
ENTRADA_INVALIDA e TABULEIRO_INVALIDO.

Na POO, esses estados continuam existindo em ResultadoSudoku, mas
TabuleiroSudoku.definir também protege sua própria operação: lança
IndexError para uma posição fora do tabuleiro e ValueError para um valor
fora do intervalo permitido. Assim, há validação tanto no fluxo da
aplicação quanto na própria operação que modifica o objeto.

### 2.9 Efeitos colaterais

O principal efeito colateral da versão imperativa é a alteração direta
do tabuleiro recebido pela função resolver. Uma chamada pode mudar a
lista que foi passada pelo chamador.

Na POO, o solucionador também modifica o tabuleiro, portanto ainda
existem efeitos colaterais sobre o objeto. Entretanto, o estado interno
é mais controlado: o construtor faz cópia defensiva e como_lista devolve
outra cópia, evitando exposição direta de `_valores`.

### 2.10 Facilidade para testar

Na versão imperativa, funções pequenas como entrada_valida,
numero_valido e encontrar_vazio podem ser testadas diretamente com
entradas e saídas conhecidas. Isso torna testes unitários simples.

Na POO, além de testar comportamentos de validação e resolução, é
possível testar cada responsabilidade separadamente. O projeto POO
produzido inclui test_sudoku.py com testes usando unittest, inclusive um
teste de cópia defensiva para verificar encapsulamento. A separação
entre validador, tabuleiro e solucionador também facilita substituir
componentes durante testes.

### 2.11 Organização do código

O imperativo possui organização linear e compacta: as funções aparecem
no mesmo módulo e o fluxo pode ser acompanhado de cima para baixo. Isso
combina bem com um problema pequeno e com um algoritmo procedural como o
backtracking.

Na POO, a organização é baseada em entidades e responsabilidades. O
código fica mais longo, mas os conceitos do sistema aparecem
explicitamente como classes. Isso pode facilitar a navegação quando o
projeto cresce.

### 2.12 Complexidade

A implementação imperativa tem menor complexidade estrutural: existem
menos abstrações e menos elementos para compreender. Para o Sudoku
atual, isso torna a resolução especialmente direta.

A versão POO acrescenta classes, métodos, injeção de dependências, uma
classe abstrata e relações de colaboração. Isso aumenta a complexidade
estrutural inicial. Em compensação, essa estrutura cria pontos de
extensão e separa melhor as responsabilidades. Quanto ao algoritmo de
resolução, a ideia fundamental do backtracking continua praticamente a
mesma nas duas versões.

## 3. Comparação resumida

  -----------------------------------------------------------------------
  Aspecto                 Imperativo              Orientado a objetos
  ----------------------- ----------------------- -----------------------
  Estado                  Matriz/lista passada    Estado encapsulado em
                          entre funções.          TabuleiroSudoku.

  Mutabilidade            Alteração direta da     Alteração pelo método
                          matriz.                 definir.

  Fluxo                   Sequência explícita de  Colaboração entre
                          funções.                objetos.

  Decomposição            Funções.                Classes e
                                                  responsabilidades.

  Reutilização            Reutilização de         Abstrações e
                          funções.                componentes
                                                  substituíveis.

  Manutenção              Simples em projeto      Responsabilidades mais
                          pequeno.                isoladas.

  Extensão                Exige adaptar funções e Pode adicionar novas
                          fluxo.                  estratégias de
                                                  solucionador.

  Erros                   Validações e retornos   Validações, estados e
                          de estado.              exceções em definir.

  Efeitos colaterais      Matriz recebida é       Objeto é mutável, mas
                          modificada diretamente. estado interno é
                                                  protegido.

  Testes                  Funções pequenas são    Componentes podem ser
                          fáceis de testar.       testados separadamente.

  Organização             Linear e compacta.      Distribuída por
                                                  classes.

  Complexidade            Menor complexidade      Mais abstrações e
                          estrutural.             estrutura.
  -----------------------------------------------------------------------

## 4. Respostas às perguntas propostas

### 4.1 Qual problema ficou mais fácil de expressar de forma imperativa?

A lógica do backtracking ficou mais direta de expressar de forma
imperativa. Na função resolver, o programa encontra uma posição vazia,
percorre os números de 1 a 9, testa se o número é válido, altera
diretamente a matriz, chama resolver novamente e, se a tentativa falhar,
desfaz a alteração colocando 0. Essa sequência corresponde naturalmente
ao estilo de comandos e mudanças explícitas de estado do paradigma
imperativo.

### 4.2 Qual problema ficou mais fácil de expressar utilizando orientação a objetos?

A organização das responsabilidades e o controle do estado ficaram mais
naturais na orientação a objetos. O tabuleiro passou a ser representado
por TabuleiroSudoku, as regras foram concentradas em ValidadorSudoku, a
estratégia de resolução foi representada por SolucionadorSudoku e
SolucionadorBacktracking, e a coordenação ficou em AplicacaoSudoku.
Assim, cada componente passou a ter um papel mais explícito.

### 4.3 Onde a orientação a objetos realmente trouxe vantagem?

A principal vantagem apareceu na separação de responsabilidades, no
encapsulamento e na possibilidade de extensão. TabuleiroSudoku protege
`_valores` com cópias defensivas e métodos de acesso; ValidadorSudoku
isola as regras; e a abstração SolucionadorSudoku permite que
AplicacaoSudoku trabalhe com diferentes estratégias de resolução sem
depender diretamente do backtracking. Isso seria especialmente útil se o
projeto crescesse.

### 4.4 Em quais situações a utilização de objetos acrescentou complexidade desnecessária?

Para operações pequenas e diretas, a POO acrescentou estrutura que não
era estritamente necessária para resolver o Sudoku atual. Por exemplo,
localizar uma casa vazia ou alterar uma posição exige passar pelo objeto
e seus métodos, enquanto no imperativo isso é feito diretamente sobre a
matriz. A classe abstrata SolucionadorSudoku e a injeção do validador
também aumentam a quantidade de conceitos e código para um projeto que
atualmente possui apenas uma estratégia de resolução. Essa complexidade
tem finalidade de organização e extensão, mas não é necessária para o
backtracking funcionar.

### 4.5 Que partes do problema praticamente não mudaram entre as duas implementações?

As regras fundamentais do Sudoku e o algoritmo de backtracking
praticamente não mudaram. As duas versões procuram uma posição vazia,
testam valores de 1 a 9, verificam linha, coluna e bloco 3×3, colocam um
valor, continuam recursivamente e desfazem a tentativa quando
necessário. Também permanecem os mesmos resultados semânticos: entrada
inválida, tabuleiro inválido, já resolvido, solucionado e sem solução.

### 4.6 Que partes precisaram ser completamente remodeladas?

A representação e a organização das responsabilidades foram remodeladas.
A matriz manipulada diretamente por funções passou a ser o estado de
TabuleiroSudoku. A validação, antes distribuída em funções como
entrada_valida, numero_valido e tabuleiro_inicial_valido, foi
reorganizada entre métodos do tabuleiro e ValidadorSudoku. A função
processar_sudoku deu lugar à coordenação de AplicacaoSudoku, e a função
resolver foi transformada no comportamento de uma abstração de
solucionador, concretizada por SolucionadorBacktracking.

## 5. Conclusão

As duas implementações resolvem o mesmo problema e preservam a mesma
lógica central de backtracking, mas apresentam formas diferentes de
estruturar a solução. A implementação imperativa é mais curta e torna
explícita a sequência de operações e mudanças na matriz. A implementação
orientada a objetos exige mais estrutura, porém distribui o sistema em
responsabilidades, protege melhor o estado interno e cria pontos de
extensão, especialmente pela abstração do solucionador. Dessa forma, a
comparação mostra que a mudança de paradigma não exige necessariamente
mudar o algoritmo principal, mas pode mudar profundamente a maneira como
o programa representa o estado e organiza as responsabilidades.

## 6. Referências ao código produzido

Implementação imperativa analisada: imperativo/sudoku.py (Etapa 03).
Implementação orientada a objetos analisada: poo/sudoku.py e
poo/test_sudoku.py (Etapa 04). Enunciado utilizado: ETAPA 05 ---
Comparação entre Imperativo e POO.
