"""Implementação imperativa de um solucionador de Sudoku 9x9.

0 representa uma posição vazia.
"""


def entrada_valida(tabuleiro):
    if not isinstance(tabuleiro, list) or len(tabuleiro) != 9:
        return False

    for linha in tabuleiro:
        if not isinstance(linha, list) or len(linha) != 9:
            return False
        for valor in linha:
            if not isinstance(valor, int) or isinstance(valor, bool):
                return False
            if valor < 0 or valor > 9:
                return False

    return True


def numero_valido(tabuleiro, linha, coluna, numero):
    # Verifica a linha.
    for c in range(9):
        if c != coluna and tabuleiro[linha][c] == numero:
            return False

    # Verifica a coluna.
    for l in range(9):
        if l != linha and tabuleiro[l][coluna] == numero:
            return False

    # Verifica a região 3x3.
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3

    for l in range(inicio_linha, inicio_linha + 3):
        for c in range(inicio_coluna, inicio_coluna + 3):
            if (l != linha or c != coluna) and tabuleiro[l][c] == numero:
                return False

    return True


def tabuleiro_inicial_valido(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            valor = tabuleiro[linha][coluna]
            if valor != 0 and not numero_valido(tabuleiro, linha, coluna, valor):
                return False
    return True


def encontrar_vazio(tabuleiro):
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro[linha][coluna] == 0:
                return linha, coluna
    return None


def resolver(tabuleiro):
    vazio = encontrar_vazio(tabuleiro)

    if vazio is None:
        return True

    linha, coluna = vazio

    for numero in range(1, 10):
        if numero_valido(tabuleiro, linha, coluna, numero):
            # Alteração explícita do estado do tabuleiro.
            tabuleiro[linha][coluna] = numero

            if resolver(tabuleiro):
                return True

            # Backtracking: desfaz a tentativa que não levou à solução.
            tabuleiro[linha][coluna] = 0

    return False


def tabuleiro_completo(tabuleiro):
    for linha in tabuleiro:
        for valor in linha:
            if valor == 0:
                return False
    return True


def processar_sudoku(tabuleiro):
    """Aplica o contrato semântico definido para o projeto."""
    if not entrada_valida(tabuleiro):
        return "ENTRADA_INVALIDA"

    if not tabuleiro_inicial_valido(tabuleiro):
        return "TABULEIRO_INVALIDO"

    if tabuleiro_completo(tabuleiro):
        return "JA_RESOLVIDO"

    if resolver(tabuleiro):
        return "SOLUCIONADO"

    return "SEM_SOLUCAO"


def imprimir_tabuleiro(tabuleiro):
    for linha in range(9):
        if linha != 0 and linha % 3 == 0:
            print("------+-------+------")

        for coluna in range(9):
            if coluna != 0 and coluna % 3 == 0:
                print("|", end=" ")
            print(tabuleiro[linha][coluna], end=" ")
        print()


def main():
    # Exemplo da Etapa 02. Troque esta matriz para testar outros casos.
    tabuleiro = [
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

    resultado = processar_sudoku(tabuleiro)
    print("Resultado:", resultado)

    if resultado == "SOLUCIONADO" or resultado == "JA_RESOLVIDO":
        imprimir_tabuleiro(tabuleiro)


if __name__ == "__main__":
    main()
