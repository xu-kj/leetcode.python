from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = [[0 for i in range(amount + 1)] for j in range(len(coins))]

        for i, c in enumerate(coins):
            for a in range(amount + 1):
                if i == 0:
                    mem[i][a] = 1 if a % c == 0 else 0
                    continue

                mem[i][a] = mem[i - 1][a]
                if c <= a:
                    mem[i][a] += mem[i][a - c] # unbounded knapsack so can keep using current item, so use mem[i][a - c] instead of mem[i - 1][a - c] here

        return mem[-1][amount]
