from typing import List

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        low, high = pricing
        next_level = [start]
        results = []

        while next_level and len(results) < k:
            level, next_level = next_level, []

            picked = []
            for row, column in level:
                price = grid[row][column]
                if price == 0:
                    continue

                if price >= low and price <= high:
                    picked.append((price, row, column))
                grid[row][column] = 0

                if row + 1 < len(grid) and grid[row + 1][column] > 0:
                    next_level.append([row + 1, column])
                if row - 1 >= 0 and grid[row - 1][column] > 0:
                    next_level.append([row - 1, column])
                if column + 1 < len(grid[0]) and grid[row][column + 1] > 0:
                    next_level.append([row, column + 1])
                if column - 1 >= 0 and grid[row][column - 1] > 0:
                    next_level.append([row, column - 1])

            picked = sorted(picked)
            for _, row, column in picked:
                if len(results) == k:
                    break

                results.append([row, column])

        return results
