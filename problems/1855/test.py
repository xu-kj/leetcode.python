import copy
from v1 import Solution

test_cases = [
    (
        [55,30,5,4,2],
        [100,20,10,10,5],
        2,
    ),
    (
        [2,2,2],
        [10,10,1],
        1,
    ),
    (
        [30,29,19,5],
        [25,25,25,25,25],
        2,
    ),
]

for nums1, nums2, expected in test_cases:
    res = Solution().maxDistance(copy.deepcopy(nums1), copy.deepcopy(nums2))
    if res != expected:
        res = Solution().maxDistance(copy.deepcopy(nums1), copy.deepcopy(nums2))
