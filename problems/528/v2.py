from typing import *
from random import shuffle


# Memory Limit Exceeded
class Solution:

    def __init__(self, w: List[int]):
        self.picks = []
        for i, wi in enumerate(w):
            self.picks.extend([i for ii in range(wi)])
        shuffle(self.picks)
        self.pick = 0

    def pickIndex(self) -> int:
        pick = self.pick
        self.pick += 1

        return self.picks[pick % len(self.picks)]


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
