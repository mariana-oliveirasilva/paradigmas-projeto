import unittest

try:
    from .sudoku import (
        AplicacaoSudoku,
        ResultadoSudoku,
        SolucionadorBacktracking,
        TabuleiroSudoku,
        ValidadorSudoku,
    )
except ImportError:
    from sudoku import (
        AplicacaoSudoku,
        ResultadoSudoku,
        SolucionadorBacktracking,
        TabuleiroSudoku,
        ValidadorSudoku,
    )


SOLUCAO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


class TestSudokuOO(unittest.TestCase):
    def setUp(self):
        self.validador = ValidadorSudoku()
        self.solucionador = SolucionadorBacktracking(self.validador)
        self.app = AplicacaoSudoku(self.validador, self.solucionador)

    def test_resolve_sudoku_normal(self):
        entrada = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        resultado, tabuleiro = self.app.executar(entrada)
        self.assertEqual(ResultadoSudoku.SOLUCIONADO, resultado)
        self.assertEqual(SOLUCAO, tabuleiro.como_lista())

    def test_uma_posicao_vazia(self):
        entrada = [linha[:] for linha in SOLUCAO]
        entrada[0][8] = 0
        resultado, tabuleiro = self.app.executar(entrada)
        self.assertEqual(ResultadoSudoku.SOLUCIONADO, resultado)
        self.assertEqual(SOLUCAO, tabuleiro.como_lista())

    def test_ja_resolvido(self):
        resultado, tabuleiro = self.app.executar(SOLUCAO)
        self.assertEqual(ResultadoSudoku.JA_RESOLVIDO, resultado)
        self.assertEqual(SOLUCAO, tabuleiro.como_lista())

    def test_dimensao_invalida(self):
        entrada = [[0] * 9 for _ in range(8)]
        resultado, tabuleiro = self.app.executar(entrada)
        self.assertEqual(ResultadoSudoku.ENTRADA_INVALIDA, resultado)
        self.assertIsNone(tabuleiro)

    def test_valor_fora_do_intervalo(self):
        entrada = [[0] * 9 for _ in range(9)]
        entrada[0][0] = 10
        resultado, tabuleiro = self.app.executar(entrada)
        self.assertEqual(ResultadoSudoku.ENTRADA_INVALIDA, resultado)
        self.assertIsNone(tabuleiro)

    def test_tabuleiro_com_repeticao(self):
        entrada = [linha[:] for linha in SOLUCAO]
        entrada[0][0] = entrada[0][1]
        resultado, tabuleiro = self.app.executar(entrada)
        self.assertEqual(ResultadoSudoku.TABULEIRO_INVALIDO, resultado)
        self.assertIsNone(tabuleiro)

    def test_encapsulamento_por_copia(self):
        entrada = [linha[:] for linha in SOLUCAO]
        tabuleiro = TabuleiroSudoku(entrada)
        entrada[0][0] = 9
        self.assertEqual(5, tabuleiro.obter(0, 0))

        copia = tabuleiro.como_lista()
        copia[0][0] = 9
        self.assertEqual(5, tabuleiro.obter(0, 0))


if __name__ == "__main__":
    unittest.main()
