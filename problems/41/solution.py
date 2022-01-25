import math
from typing import *


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lowerbound = math.inf
        upperbound = -math.inf
        positives = set([num for num in nums if num > 0])
        for num in positives:
            if num > 0:
                lowerbound = min(lowerbound, num)
                upperbound = max(upperbound, num)
        if math.isinf(lowerbound) or lowerbound > 1:
            return 1

        if len(positives) == upperbound - lowerbound + 1:
            return upperbound + 1

        upperbound = min(upperbound + 1, lowerbound + int(5e5))
        missing = (1 << (upperbound - lowerbound)) - 1  # max 5e5
        for num in nums:
            if num <= 0 or num >= upperbound:
                continue

            num -= lowerbound
            if missing & (1 << num):
                missing -= (1 << num)

        for i in range(upperbound - lowerbound):
            if missing & (1 << i):
                return int(lowerbound + i)
        return upperbound


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
        res = sol.firstMissingPositive(t[0])
        tf = res == t[1]
        if not tf:
            sol.firstMissingPositive(t[0])
