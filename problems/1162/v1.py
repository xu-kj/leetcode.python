from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        copy = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

        total = len(grid) * len(grid[0])
        water = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    water += 1
                else:
                    copy[i][j] = 1

                    if i - 1 >= 0:
                        copy[i - 1][j] = 1
                    if i + 1 < len(grid):
                        copy[i + 1][j] = 1
                    if j - 1 >= 0:
                        copy[i][j - 1] = 1
                    if j + 1 < len(grid[0]):
                        copy[i][j + 1] = 1

        if water == 0 or water == total:
            return -1

        t = self.maxDistance(copy)
        return 1 if t == -1 else t + 1
