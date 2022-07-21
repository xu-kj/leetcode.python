from math import inf, isinf
from typing import List


# F(amount) = F(amount - coin) + 1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [0] * (amount + 1)

        # bottom-up memoization
        for a in range(1, amount + 1):
            mem[a] = inf

            for c in coins:
                if c > a:
                    continue

                mem[a] = min(mem[a], mem[a - c] + 1)

        result = mem[amount]
        return -1 if isinf(result) else result
