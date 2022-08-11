import copy
from v2 import Solution

test_cases = [
    (
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]],
        2
    ),
    (
        [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]],
        4
    ),
    (
        [
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 0]],
        2
    ),
]

for grid, expected in test_cases:
    res = Solution().maxDistance(copy.deepcopy(grid))
    if res != expected:
        Solution().maxDistance(copy.deepcopy(grid))
