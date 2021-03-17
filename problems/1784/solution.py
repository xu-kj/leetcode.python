from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s = {}
        for num in nums:
            s[num] = s.get(num, 0) + 1
        return sum([key for key in s.keys() if s[key] == 1])
