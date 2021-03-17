from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x: int, y: int) -> int:
            if x < 0 or x >= len(grid):
                return 0
            if y < 0 or y >= len(grid[x]):
                return 0
            if grid[x][y] == '0':
                return 0

            grid[x][y] = '0'
            return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)

        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                islands.append(dfs(i, j))
        return sum([1 if island else 0 for island in islands])
