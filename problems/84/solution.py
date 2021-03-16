from typing import *

import sys


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hs = []
        best = 0
        for i in range(len(heights)):
            height = heights[i]
            start = i

            while len(hs) > 0 and hs[-1][0] >= height:
                last = hs.pop()
                start = last[1]
                if last[0] > height:
                    best = max(best, last[0] * (i - last[1]))
            hs.append((height, start))

        areas = [h[0] * (len(heights) - h[1]) for h in hs]
        best = max(best, max(areas) if len(areas) > 0 else 0)
        return best


if __name__ == "__main__":
    test_cases = [
        (
            [2,1,5,6,2,3],
            10
        ),
        (
            [1,2,2],
            4
        ),
        (
            [1,2,3,4,5],
            9
        ),
        (
            [0,1,2,3,4,5,6,7,8],
            20
        ),
        (
            [2,1,2],
            3
        ),
        (
            [4,2,0,3,2,5],
            6
        ),
        (
            [3,5,5,2,5,5,6,6,4,4,1,1,2,5,5,6,6,4,1,3],
            24
        ),
        (
            [10,10,4,8,12,13,3,14,8,16,6,12,7,19,17,2,2,11,10,12],
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
