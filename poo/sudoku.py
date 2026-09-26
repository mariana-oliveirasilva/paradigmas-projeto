"""Etapa 04 - Solucionador de Sudoku 9x9 orientado a objetos.

O modelo separa:
- TabuleiroSudoku: estado e regras estruturais do tabuleiro;
- ValidadorSudoku: validação das regras do domínio;
- SolucionadorSudoku: abstração de uma estratégia de resolução;
- SolucionadorBacktracking: estratégia concreta de resolução;
- AplicacaoSudoku: coordenação do caso de uso e apresentação do resultado.

0 representa uma posição vazia.
"""

from abc import ABC, abstractmethod
from typing import Optional


class TabuleiroSudoku:
    TAMANHO = 9
    TAMANHO_BLOCO = 3
    VAZIO = 0

    def __init__(self, valores: list[list[int]]):
        # Cópia defensiva: o objeto controla seu próprio estado.
        self._valores = [linha[:] for linha in valores]

    def possui_dimensoes_validas(self) -> bool:
        if len(self._valores) != self.TAMANHO:
            return False

        for linha in self._valores:
            if len(linha) != self.TAMANHO:
                return False

        return True

    def possui_valores_validos(self) -> bool:
        if not self.possui_dimensoes_validas():
            return False

        for linha in self._valores:
            for valor in linha:
                # bool é subtipo de int em Python, mas não é aceito como valor do Sudoku.
                if type(valor) is not int or valor < 0 or valor > 9:
                    return False

        return True

    def obter(self, linha: int, coluna: int) -> int:
        return self._valores[linha][coluna]

    def definir(self, linha: int, coluna: int, valor: int) -> None:
        if not 0 <= linha < self.TAMANHO or not 0 <= coluna < self.TAMANHO:
            raise IndexError("Posição fora do tabuleiro.")

        if type(valor) is not int or valor < 0 or valor > 9:
            raise ValueError("O valor deve ser um inteiro entre 0 e 9.")

        self._valores[linha][coluna] = valor

    def encontrar_vazio(self) -> Optional[tuple[int, int]]:
        for linha in range(self.TAMANHO):
            for coluna in range(self.TAMANHO):
                if self._valores[linha][coluna] == self.VAZIO:
                    return linha, coluna
        return None

    def esta_completo(self) -> bool:
        return self.encontrar_vazio() is None

    def valores_da_linha(self, linha: int) -> list[int]:
        return self._valores[linha][:]

    def valores_da_coluna(self, coluna: int) -> list[int]:
        return [self._valores[linha][coluna] for linha in range(self.TAMANHO)]

    def valores_do_bloco(self, linha: int, coluna: int) -> list[int]:
        inicio_linha = (linha // self.TAMANHO_BLOCO) * self.TAMANHO_BLOCO
        inicio_coluna = (coluna // self.TAMANHO_BLOCO) * self.TAMANHO_BLOCO

        valores = []
        for i in range(inicio_linha, inicio_linha + self.TAMANHO_BLOCO):
            for j in range(inicio_coluna, inicio_coluna + self.TAMANHO_BLOCO):
                valores.append(self._valores[i][j])

        return valores

    def como_lista(self) -> list[list[int]]:
        # Não expõe a lista interna diretamente.
        return [linha[:] for linha in self._valores]

    def __str__(self) -> str:
        linhas = []
        for linha in self._valores:
            linhas.append(" ".join(str(valor) for valor in linha))
        return "\n".join(linhas)


class ValidadorSudoku:
    """Responsável pelas regras de validade do Sudoku."""

    @staticmethod
    def _sem_repeticoes(valores: list[int]) -> bool:
        preenchidos = [valor for valor in valores if valor != TabuleiroSudoku.VAZIO]
        return len(preenchidos) == len(set(preenchidos))

    def entrada_valida(self, tabuleiro: TabuleiroSudoku) -> bool:
        return (
            tabuleiro.possui_dimensoes_validas()
            and tabuleiro.possui_valores_validos()
        )

    def tabuleiro_valido(self, tabuleiro: TabuleiroSudoku) -> bool:
        if not self.entrada_valida(tabuleiro):
            return False

        for indice in range(TabuleiroSudoku.TAMANHO):
            if not self._sem_repeticoes(tabuleiro.valores_da_linha(indice)):
                return False
            if not self._sem_repeticoes(tabuleiro.valores_da_coluna(indice)):
                return False

        for linha in range(0, TabuleiroSudoku.TAMANHO, TabuleiroSudoku.TAMANHO_BLOCO):
            for coluna in range(
                0, TabuleiroSudoku.TAMANHO, TabuleiroSudoku.TAMANHO_BLOCO
            ):
                if not self._sem_repeticoes(
                    tabuleiro.valores_do_bloco(linha, coluna)
                ):
                    return False

        return True

    def pode_colocar(
        self, tabuleiro: TabuleiroSudoku, linha: int, coluna: int, valor: int
    ) -> bool:
        if valor in tabuleiro.valores_da_linha(linha):
            return False

        if valor in tabuleiro.valores_da_coluna(coluna):
            return False

        if valor in tabuleiro.valores_do_bloco(linha, coluna):
            return False

        return True


class SolucionadorSudoku(ABC):
    """Abstração de uma estratégia de resolução."""

    @abstractmethod
    def resolver(self, tabuleiro: TabuleiroSudoku) -> bool:
        """Resolve o tabuleiro recebido, retornando True se houver solução."""
        raise NotImplementedError


class SolucionadorBacktracking(SolucionadorSudoku):
    """Estratégia concreta que resolve o Sudoku por backtracking."""

    def __init__(self, validador: ValidadorSudoku):
        # Composição/colaboração: a estratégia utiliza um validador.
        self._validador = validador

    def resolver(self, tabuleiro: TabuleiroSudoku) -> bool:
        posicao = tabuleiro.encontrar_vazio()

        if posicao is None:
            return True

        linha, coluna = posicao

        for valor in range(1, 10):
            if self._validador.pode_colocar(tabuleiro, linha, coluna, valor):
                tabuleiro.definir(linha, coluna, valor)

                if self.resolver(tabuleiro):
                    return True

                tabuleiro.definir(linha, coluna, TabuleiroSudoku.VAZIO)

        return False


class ResultadoSudoku:
    ENTRADA_INVALIDA = "ENTRADA_INVALIDA"
    TABULEIRO_INVALIDO = "TABULEIRO_INVALIDO"
    JA_RESOLVIDO = "JA_RESOLVIDO"
    SOLUCIONADO = "SOLUCIONADO"
    SEM_SOLUCAO = "SEM_SOLUCAO"


class AplicacaoSudoku:
    """Coordena validação e resolução sem concentrar as regras em uma única classe."""

    def __init__(
        self,
        validador: ValidadorSudoku,
        solucionador: SolucionadorSudoku,
    ):
        self._validador = validador
        # Dependência pela abstração permite trocar a estratégia de resolução.
        self._solucionador = solucionador

    def executar(self, valores: list[list[int]]) -> tuple[str, Optional[TabuleiroSudoku]]:
        tabuleiro = TabuleiroSudoku(valores)

        if not self._validador.entrada_valida(tabuleiro):
            return ResultadoSudoku.ENTRADA_INVALIDA, None

        if not self._validador.tabuleiro_valido(tabuleiro):
            return ResultadoSudoku.TABULEIRO_INVALIDO, None

        if tabuleiro.esta_completo():
            return ResultadoSudoku.JA_RESOLVIDO, tabuleiro

        if self._solucionador.resolver(tabuleiro):
            return ResultadoSudoku.SOLUCIONADO, tabuleiro

        return ResultadoSudoku.SEM_SOLUCAO, None


def main() -> None:
    valores = [
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

    validador = ValidadorSudoku()
    solucionador = SolucionadorBacktracking(validador)
    aplicacao = AplicacaoSudoku(validador, solucionador)

    resultado, tabuleiro = aplicacao.executar(valores)

    print(resultado)
    if tabuleiro is not None:
        print(tabuleiro)


if __name__ == "__main__":
    main()
