from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= len(board):
                return
            if y < 0 or y >= len(board[0]):
                return

            if board[x][y] == 'O':
                board[x][y] = 'B'
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        for i in [0, len(board) - 1]:
            for j in range(len(board[i])):
                dfs(i, j)
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
