import copy
from v1 import Solution

test_cases = [
    (
        [
            [1,2,0,1],
            [1,3,0,1],
            [0,2,5,1],
        ],
        [2,5],
        [0,0],
        3,
        [[0,1],[1,1],[2,1]],
    ),
    (
        [
            [1,2,0,1],
            [1,3,3,1],
            [0,2,5,1],
        ],
        [2,3],
        [2,3],
        2,
        [[2,1],[1,2]],
    ),
    (
        [
            [1,1,1],
            [0,0,1],
            [2,3,4],
        ],
        [2,3],
        [0,0],
        3,
        [[2,1],[2,0]],
    ),
]

for grid, pricing, start, k, expected in test_cases:
    res = Solution().highestRankedKItems(copy.deepcopy(grid), copy.deepcopy(pricing), copy.deepcopy(start), k)
    if res != expected:
        Solution().highestRankedKItems(copy.deepcopy(grid), copy.deepcopy(pricing), copy.deepcopy(start), k)
