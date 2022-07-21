# from v1 import Solution
# from v2 import Solution
# from v3 import Solution
from v4 import Solution

test_cases = [
    (
        [1, 2, 5], 11,
        3
    ),
    (
        [2], 3,
        -1
    ),
    (
        [1], 0,
        0
    ),
    (
        [3, 7, 405, 436], 8839,
        25
    ),
    (
        [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422], 9864,
        24
    ),
    (
        [278, 274, 153, 490], 8633,
        25
    ),
    (
        [27, 40, 244, 168, 383], 6989,
        23
    ),
    (
        [80, 149, 71, 111], 8683,
        61
    ),
]

for coins, amount, expected in test_cases:
    res = Solution().coinChange(coins, amount)
    if res != expected:
        Solution().coinChange(coins, amount)
