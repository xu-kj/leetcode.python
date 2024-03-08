# from v1 import Solution
from v2 import Solution

if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
        ([[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]], [[2, 4], [5, 5]]),
        ([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]], [[1, 3], [4, 7]]),
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.merge(t[0])
        tf = res == t[1]
        if not tf:
            sol.merge(t[0])
