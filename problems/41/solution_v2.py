import math
from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lowerbound = math.inf
        for i in range(len(nums)):
            num = nums[i]
            if num > 0:
                lowerbound = min(lowerbound, num)
            else:
                nums[i] = 1
        if math.isinf(lowerbound) or lowerbound > 1:
            return 1

        # the array will only contain [1, len(nums)]
        # if the number exists, mark the number at that index as negative
        for num in nums:
            num = abs(num)
            if num > len(nums) or nums[num - 1] < 0:
                continue

            nums[num - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([2147483647], 1),
        ([1, 1], 2),
        ([99, 94, 96, 11, 92, 5, 91, 89, 57, 85, 66, 63, 84, 81, 79, 61, 74, 78, 77, 30, 64, 13, 58, 18, 70, 69, 51, 12, 32, 34, 9, 43, 39, 8, 1, 38, 49, 27, 21, 45, 47, 44, 53, 52, 48, 19, 50, 59, 3, 40, 31,
         82, 23, 56, 37, 41, 16, 28, 22, 33, 65, 42, 54, 20, 29, 25, 10, 26, 4, 60, 67, 83, 62, 71, 24, 35, 72, 55, 75, 0, 2, 46, 15, 80, 6, 36, 14, 73, 76, 86, 88, 7, 17, 87, 68, 90, 95, 93, 97, 98], 100),
        ([0], 1),
        ([1, 3, 3], 2),
        ([1, 2, 3, 10, 2147483647, 9], 4)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.firstMissingPositive(t[0].copy())
        tf = res == t[1]
        if not tf:
            sol.firstMissingPositive(t[0])
