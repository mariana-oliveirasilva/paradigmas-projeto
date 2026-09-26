# Etapa 04 — Reflexão sobre a implementação orientada a objetos

## Como meu modelo mudou ao passar do paradigma imperativo para o orientado a objetos?

Na implementação imperativa, o problema era representado principalmente por uma matriz e por subprogramas que operavam diretamente sobre esse estado. O fluxo da resolução tinha papel central: localizar uma posição vazia, testar valores, modificar a matriz e desfazer a modificação quando uma tentativa não levava a uma solução.

Na implementação orientada a objetos, o foco da modelagem passou para os elementos do domínio e para as responsabilidades de cada componente. O tabuleiro deixou de ser apenas uma lista manipulada por funções externas e passou a ser representado por um objeto `TabuleiroSudoku`, responsável por manter e disponibilizar seu próprio estado. As regras de validade ficaram concentradas em `ValidadorSudoku`, enquanto a resolução passou a ser responsabilidade de objetos que seguem a abstração `SolucionadorSudoku`.

Dessa forma, a versão orientada a objetos não é apenas a implementação imperativa colocada dentro de uma classe. O problema foi reorganizado em objetos que colaboram entre si.

## Representação do estado

O estado principal continua sendo formado pelos 81 valores do Sudoku, porém agora ele pertence ao objeto `TabuleiroSudoku`.

A matriz interna é armazenada no atributo `_valores`. O acesso e a modificação do estado ocorrem por operações do próprio objeto, como `obter`, `definir`, `encontrar_vazio`, `valores_da_linha`, `valores_da_coluna` e `valores_do_bloco`.

O construtor cria uma cópia dos valores recebidos e o método `como_lista` também devolve uma cópia. Assim, a lista interna não é exposta diretamente para outros componentes.

## Responsabilidades

As responsabilidades foram separadas da seguinte maneira:

- `TabuleiroSudoku`: representa o tabuleiro e controla o acesso ao seu estado.
- `ValidadorSudoku`: conhece as regras que determinam se a entrada e o estado do Sudoku são válidos e se um valor pode ocupar determinada posição.
- `SolucionadorSudoku`: define a abstração de uma estratégia capaz de resolver um Sudoku.
- `SolucionadorBacktracking`: implementa a estratégia concreta de resolução por backtracking.
- `AplicacaoSudoku`: coordena o caso de uso, decidindo quando validar, quando reconhecer um tabuleiro já resolvido e quando solicitar sua resolução.
- `ResultadoSudoku`: centraliza os resultados semânticos utilizados no contrato definido na Etapa 02.

Essa separação evita que uma única classe concentre todas as decisões do sistema.

## Relacionamento entre componentes

A solução utiliza principalmente composição e colaboração entre objetos.

`AplicacaoSudoku` recebe um `ValidadorSudoku` e um objeto que respeita a abstração `SolucionadorSudoku`. O `SolucionadorBacktracking`, por sua vez, utiliza um `ValidadorSudoku` para verificar se determinada tentativa é permitida.

O tabuleiro é passado entre esses componentes como o objeto que representa o estado do problema.

A composição foi preferida sempre que a relação entre os elementos não representa uma relação do tipo "é um". Por exemplo, um validador não é um tabuleiro e um tabuleiro não é um solucionador, portanto herança entre esses componentes não seria adequada.

## Encapsulamento

O encapsulamento aparece principalmente em `TabuleiroSudoku`. Seu estado interno é mantido em `_valores` e os outros componentes não precisam conhecer a forma exata como esse estado é armazenado para executar operações do domínio.

A classe fornece operações específicas para consultar linhas, colunas, blocos, posições vazias e alterar valores. Também utiliza cópias defensivas para evitar que código externo receba a referência da matriz interna e a modifique sem passar pelas operações do objeto.

Isso reduz o acoplamento entre a representação interna do tabuleiro e as demais partes do programa.

## Abstração e polimorfismo

`SolucionadorSudoku` é uma classe abstrata que representa a ideia de uma estratégia de resolução. Ela define a operação `resolver`, sem determinar qual algoritmo deve ser utilizado.

`SolucionadorBacktracking` é uma implementação concreta dessa abstração. `AplicacaoSudoku` depende de `SolucionadorSudoku`, e não diretamente de `SolucionadorBacktracking`.

Com isso, objetos de diferentes solucionadores podem ser utilizados pela aplicação por meio da mesma operação `resolver`. Esse é o principal uso de polimorfismo na solução.

## Herança

A herança aparece apenas onde existe uma relação conceitual adequada: `SolucionadorBacktracking` é um tipo de `SolucionadorSudoku`.

Não foi criada uma hierarquia como `Celula`, `Linha`, `Coluna` ou diferentes tipos artificiais de tabuleiro apenas para demonstrar herança. Isso aumentaria a complexidade sem representar melhor o problema.

A decisão segue a ideia de utilizar herança somente quando ela expressa uma especialização real. Nos demais relacionamentos, composição e colaboração foram consideradas mais adequadas.

## Reutilização

A separação de responsabilidades aumenta a possibilidade de reutilização. `ValidadorSudoku`, por exemplo, pode ser utilizado independentemente para verificar um tabuleiro, mesmo quando não se deseja resolvê-lo.

Da mesma forma, `TabuleiroSudoku` concentra operações estruturais que podem ser utilizadas por diferentes estratégias de resolução.

A abstração `SolucionadorSudoku` também permite que a aplicação utilize outras estratégias sem alterar o contrato principal do sistema.

## Extensão do sistema

A estrutura orientada a objetos permite adicionar novas estratégias de resolução criando outras implementações de `SolucionadorSudoku`.

Por exemplo, futuramente poderia existir uma estratégia diferente de resolução sem que `AplicacaoSudoku` precisasse conhecer seus detalhes internos. Desde que o novo objeto respeite a operação `resolver`, ele poderá ser utilizado no mesmo lugar que `SolucionadorBacktracking`.

Essa possibilidade demonstra uma diferença importante em relação à versão imperativa: além do fluxo de execução, a modelagem passa a considerar explicitamente responsabilidades, relações e pontos de extensão entre os componentes.

## Conclusão

A principal mudança entre as duas implementações está na forma de organizar o problema. A versão imperativa enfatiza operações e mudanças sucessivas no estado do tabuleiro. A versão orientada a objetos distribui estado e comportamento entre objetos com responsabilidades definidas.

O algoritmo de backtracking continua sendo adequado para encontrar a solução, mas agora ele é apenas uma estratégia dentro do modelo, e não o elemento responsável por organizar todo o sistema.
