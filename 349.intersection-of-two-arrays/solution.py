from typing import *


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# if __name__ == "__main__":
    # test_cases = [
    #     ([2, 7, 11, 15], 9, [1, 2]),
    #     ([0, 0, 3, 4], 0, [1, 2]),
    #     ([5, 25, 75], 100, [2, 3]),
    #     ([3, 24, 50, 79, 88, 150, 345], 200, [3, 6])
    # ]

    # sol = Solution()
    # for t in test_cases:
    #     res = sol.twoSum(t[0], t[1])
    #     tf = res == t[2]
    #     if not tf:
    #         sol.twoSum(t[0], t[1])
