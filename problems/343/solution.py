class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        dp = [1] * (n + 1)
        dp[2], dp[3] = 2, 3  # 2 and 3 are the basic units
        for i in range(4, n + 1):
            dp[i] = max(2 * dp[i - 2], 3 * dp[i - 3])
        return dp[n]


if __name__ == "__main__":
    test_cases = [
        (2, 1),
        (10, 36)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.integerBreak(t[0])
        tf = res == t[1]
        if not tf:
            sol.integerBreak(t[0])
