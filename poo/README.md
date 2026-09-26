# Implementação Orientada a Objetos — Etapa 04

Esta pasta contém a reimplementação orientada a objetos do Solucionador de Sudoku 9×9.

## Arquivos

- `sudoku.py`: implementação orientada a objetos.
- `reflexão.md`: reflexão obrigatória comparando a modelagem imperativa com a orientada a objetos.
- `test_sudoku.py`: testes automatizados básicos baseados no contrato da Etapa 02.

## Modelo

A solução separa o problema em:

- `TabuleiroSudoku`: estado do tabuleiro;
- `ValidadorSudoku`: regras de validação;
- `SolucionadorSudoku`: abstração para estratégias de resolução;
- `SolucionadorBacktracking`: estratégia concreta;
- `AplicacaoSudoku`: coordenação do caso de uso.

A herança é utilizada apenas entre `SolucionadorBacktracking` e `SolucionadorSudoku`, pois existe uma relação de especialização real. Nos demais casos foi utilizada composição/colaboração.

## Executar

Na raiz do repositório:

```bash
python poo/sudoku.py
```

## Testar

```bash
python -m unittest poo/test_sudoku.py -v
```
