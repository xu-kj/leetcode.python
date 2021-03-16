from typing import List
import collections

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0

        summary = {}
        for num in nums:
            summary[num] = summary.get(num, 0) + 1
        for i in range(len(nums)):
            if not summary[nums[i]]:
                continue
            summary[nums[i]] -= 1
            if k - nums[i] in summary and summary[k - nums[i]]:
                result += 1
                summary[k - nums[i]] -= 1
        return result