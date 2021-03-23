from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        last, s = None, 0
        for num in nums:
            if last is None:
                last = num
                s = num
                continue

            if num > last:
                s += num
                last = num
            else:
                max_sum = max(max_sum, s)
                last = num
                s = num

        max_sum = max(max_sum, s)
        return max_sum
