from typing import List
import collections

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        summary = collections.Counter(deliciousness)
        result = 0
        res = []

        # maximum possible sum is 2^20 + 2^20 = 2^21
        for p in range(0, 21 + 1):
            s = 2 ** p
            for i in [key for key in summary.keys() if key <= s]:
                t = summary[i]
                summary[i] -= 1
                if s - i >= i and s - i in summary:
                    result += (t * summary[s - i]) if s - i > i else ((t * summary[s - i]) / 2)
                    res.append((i, s - i))
                summary[i] += 1
        return int(result % (1e9 + 7))

if __name__ == "__main__":
    test_cases = [
        ([1,3,5,7,9], 4),
        ([1,1,1,3,3,3,7], 15),
        ([1048576,1048576], 1)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.countPairs(t[0])
        tf = res == t[1]
        if not tf:
            sol.countPairs(t[0])
