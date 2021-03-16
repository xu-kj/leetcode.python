from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_element = {}
        unwanted_stack = []
        for num in nums2:
            while unwanted_stack and unwanted_stack[-1] < num:
                n = unwanted_stack.pop()
                next_greater_element[n] = num
            unwanted_stack.append(num)
        return [next_greater_element[num] if num in next_greater_element else -1 for num in nums1]
