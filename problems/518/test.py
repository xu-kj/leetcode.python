from v1 import Solution

test_cases = [
    (
        [1, 2, 5], 5,
        4
    ),
    (
        [2], 3,
        0
    ),
    (
        [10], 10,
        1
    ),
    (
        [7], 0,
        1
    )
]

for coins, amount, expected in test_cases:
    res = Solution().change(amount, coins)
    if res != expected:
        Solution().change(amount, coins)
