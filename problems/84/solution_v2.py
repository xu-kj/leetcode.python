from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        results = [0] * len(heights)
        for i, height in enumerate(heights):
            while s and height < s[-1][1]:
                si, sh = s.pop()
                results[si] = sh * (i - 1 - (s[-1][0] if s else -1))
            s.append((i, height))
        while s:
            si, sh = s.pop()
            results[si] = sh * (len(heights) - 1 - (s[-1][0] if s else -1))
        return max(results) if results else 0


if __name__ == "__main__":
    test_cases = [
        (
            [2, 1, 5, 6, 2, 3],
            10
        ),
        (
            [1, 2, 2],
            4
        ),
        (
            [1, 2, 3, 4, 5],
            9
        ),
        (
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            20
        ),
        (
            [2, 1, 2],
            3
        ),
        (
            [4, 2, 0, 3, 2, 5],
            6
        ),
        (
            [3, 5, 5, 2, 5, 5, 6, 6, 4, 4, 1, 1, 2, 5, 5, 6, 6, 4, 1, 3],
            24
        ),
        (
            [10, 10, 4, 8, 12, 13, 3, 14, 8, 16, 6,
                12, 7, 19, 17, 2, 2, 11, 10, 12],
            48
        ),
        (
            [],
            0
        )
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.largestRectangleArea(t[0])
        if res != t[1]:
            sol.largestRectangleArea(t[0])
