from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        s = 0
        result = len(nums) + 1
        while r < len(nums):
            s += nums[r]
            r += 1
            while s >= target:
                if s - nums[l] < target:
                    result = min(result, r - l)
                s -= nums[l]
                l += 1
        return 0 if result > len(nums) else result
