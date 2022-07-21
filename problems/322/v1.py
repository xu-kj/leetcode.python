from typing import List


# backtracking, time limit exceeded, time complexity: O(amount ^ len(coins)), exponential in the number of coins
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sorted_coins = sorted(coins, reverse=True)
        return self.coinChangeInternal(sorted_coins, amount)

    def coinChangeInternal(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        min_num = -1
        for i, coin in enumerate(coins):
            if coin > amount:
                continue

            if amount % coin == 0:
                # the input coin is sorted from the largest to the smallest, num will not be smaller
                num = amount // coin
                min_num = min(min_num, num) if min_num != -1 else num
                break
            elif i == len(coins) - 1:
                continue

            for j in range(1, amount // coin + 1):
                num = self.coinChangeInternal(coins[i + 1:], amount - coin * j)
                if num != -1:
                    num += j
                    min_num = min(min_num, num) if min_num != -1 else num

        return min_num
