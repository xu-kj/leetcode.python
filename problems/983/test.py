# from v1 import Solution
from v2 import Solution

test_cases = [
    (
        [1, 4, 6, 7, 8, 20], [2, 7, 15],
        11
    ),
    (
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15],
        17
    ),
    (
        [1, 2, 3, 4, 6, 8, 9, 10, 13, 14, 16, 17,
            19, 21, 24, 26, 27, 28, 29], [3, 14, 50],
        50
    ),
]

for days, costs, expected in test_cases:
    res = Solution().mincostTickets(days, costs)
    if res != expected:
        Solution().mincostTickets(days, costs)
