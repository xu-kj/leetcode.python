from typing import *


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1, i2 = 0, len(numbers) - 1
        while i1 < i2:
            if (numbers[i1] + numbers[i2] == target):
                return [i1 + 1, i2 + 1]

            while (target - numbers[i1] < numbers[i2]):
                i2 -= 1
            while (target - numbers[i2] > numbers[i1]):
                i1 += 1


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([0, 0, 3, 4], 0, [1, 2]),
        ([5, 25, 75], 100, [2, 3]),
        ([3, 24, 50, 79, 88, 150, 345], 200, [3, 6])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.twoSum(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.twoSum(t[0], t[1])
