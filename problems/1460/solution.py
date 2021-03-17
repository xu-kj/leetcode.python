from typing import List
import collections

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # allowed to make any number of steps -> can move any element to anywhere, like bubble sort
        return collections.Counter(target) == collections.Counter(arr)