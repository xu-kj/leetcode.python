import copy
from v1 import Solution

test_cases = [
    (
        [1,2,3,4,5],
        3,
    ),
    (
        [1,2],
        1,
    ),
]

for root, expected in test_cases:
    res = Solution().diameterOfBinaryTree(copy.deepcopy(root))
    if res != expected:
        Solution().diameterOfBinaryTree(copy.deepcopy(root))
