from typing import List


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        k = 1
        c = 0
        while True:
            if k >= n / 2:
                k = (k - n / 2) * 2 + 1
            else:
                k = k * 2
            c += 1

            if k == 1:
                break
        return c


if __name__ == "__main__":
    test_cases = [
        (2, 1),
        (4, 2),
        (6, 4)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.reinitializePermutation(t[0])
        if res != t[1]:
            sol.reinitializePermutation(t[0])
