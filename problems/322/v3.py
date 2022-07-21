from math import inf, isinf
from typing import List


# F(amount) = F(amount - coin) + 1
# knapsack dp, O(n * W^2), time limit exceeded
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [[0] * (amount + 1) for i in range(len(coins))]
        for i, c in enumerate(coins):
            for a in range(1, amount + 1):  # return 0 when amount is 0
                if i == 0:  # initialize tabulation
                    if c > a:
                        dp[i][a] = inf
                    else:
                        dp[i][a] = a // c if a % c == 0 else inf
                    continue

                if c > a:  # c cannot fit in the backpack, ignore
                    dp[i][a] = dp[i - 1][a]
                else:
                    dp[i][a] = dp[i - 1][a]
                    for j in range(1, a // c + 1):  # time complexity: a / c
                        dp[i][a] = min(dp[i][a], dp[i - 1][a - j * c] + j)

        result = dp[-1][amount]
        return -1 if isinf(result) else result
