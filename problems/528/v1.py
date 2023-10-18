from typing import *
from random import choices


class Solution:

    def __init__(self, w: List[int]):
        self.count = len(w)
        self.weights = w

    def pickIndex(self) -> int:
        return choices(range(self.count), weights=self.weights)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

weights = [1, 3]
sol = Solution(weights)
print(sol.pickIndex())
