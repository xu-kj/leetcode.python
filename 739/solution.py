from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        unwanted_stack = []
        for i, t in enumerate(T):
            while unwanted_stack and T[unwanted_stack[-1]] < t:
                index = unwanted_stack.pop()
                result[index] = i - index
            unwanted_stack.append(i)
        return result
