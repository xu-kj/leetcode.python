from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            distance = 0
            for j in range(len(grid[i])):
                if distance > 0:
                    distance += 1

                distance = self.f(grid, i, j, distance)

            distance = 0
            for j in range(len(grid[i])).__reversed__():
                if distance > 0:
                    distance += 1

                distance = self.f(grid, i, j, distance)

        for j in range(len(grid[0])):
            distance = 0
            for i in range(len(grid)):
                if distance > 0:
                    distance += 1

                distance = self.f(grid, i, j, distance)

            distance = 0
            for i in range(len(grid)).__reversed__():
                if distance > 0:
                    distance += 1

                distance = self.f(grid, i, j, distance)

        max_distance = 0
        for row in grid:
            max_distance = max(max_distance, max(row))
        return max_distance - 1 if max_distance > 1 else -1

    def f(self, grid: List[List[int]], i: int, j: int, distance: int) -> int:
        if distance == 0:
            return grid[i][j] if grid[i][j] > 0 else distance

        if grid[i][j] > 0 and grid[i][j] < distance:
            return grid[i][j]
        else:
            grid[i][j] = distance
            return distance
