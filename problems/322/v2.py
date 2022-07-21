from typing import List


# F(amount) = F(amount - coin) + 1
class Solution:
    def __init__(self):
        self.mem = {}

    # RecursionError: maximum recursion depth exceeded while calling a Python object
    # top-down memoization does not reduce the worst-case number of stacks generated during recursion
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        min_num = -1
        for coin in coins:
            if coin > amount:
                continue
            if amount % coin == 0:
                num = amount // coin
                min_num = min(min_num, num) if min_num != -1 else num
                continue

            remainder = amount - coin
            if remainder not in self.mem:
                self.mem[remainder] = self.coinChange(coins, remainder)

            if self.mem[remainder] != -1:
                num = self.mem[remainder] + 1
                min_num = min(min_num, num) if min_num != -1 else num

        return min_num
