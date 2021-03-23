from typing import List
import collections
import functools
import math


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        summary = collections.Counter(deck)
        gcd = functools.reduce(lambda x, y: math.gcd(x, y), summary.values())
        return gcd >= 2


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 4, 3, 2, 1], True),
        ([1, 1, 1, 2, 2, 2, 3, 3], False),
        ([1], False),
        ([1, 1], True),
        ([1, 1, 2, 2, 2, 2], True)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.hasGroupsSizeX(t[0])
        tf = res == t[1]
        if not tf:
            sol.hasGroupsSizeX(t[0])
