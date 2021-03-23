from typing import List
import collections


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        summary = collections.Counter(deck)
        m = min(summary.values())
        for i in range(2, m + 1):
            if m % i != 0:
                continue

            check = True
            s = 0
            for count in summary.values():
                if count % i != 0:
                    check = False
                    break

                s += count // i

            if check:
                return True
        return False


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
