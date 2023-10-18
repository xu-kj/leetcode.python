from typing import *
from itertools import accumulate
from bisect import bisect_left
import random


class Solution:

    def __init__(self, w: List[int]):
        self.weights = list(accumulate(w))
        self.tw = sum(w)

    def pickIndex(self) -> int:
        pick = random.randint(1, self.tw)
        i = bisect_left(self.weights, pick)
        return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

weights = [1, 3]
sol = Solution(weights)
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
