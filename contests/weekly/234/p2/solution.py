from typing import List


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        def getNewArray(p: List[int]) -> List[int]:
            result = []
            for k in range(n // 2):
                result.append(p[k])
                result.append(p[n // 2 + k])
            return result

        original = list(range(n))
        new = original
        c = 0
        while True:
            perm = new
            new = getNewArray(perm)
            c += 1

            if all([new[i] == original[i] for i in range(n)]):
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
