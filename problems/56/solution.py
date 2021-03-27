from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,2], [3,4], [2,3]] should give [[1,4]]
        # sort the intervals by lowerbound first, so each time we are inserting
        # the "nearest" interval into the array to merge
        intervals.sort(key=lambda interval: interval[0])
        r = [intervals[0]] if len(intervals) > 0 else None
        for interval in intervals:
            merged = self.mergeTwoRanges(r[-1], interval)
            if merged:
                r[-1] = merged
            else:
                r.append(interval)
        return r

    def mergeTwoRanges(self, iLeft: List[int], iRight: List[int]) -> List[int]:
        left, right = [], []
        if iLeft[0] < iRight[0]:
            left, right = iLeft, iRight
        elif iLeft[0] == iRight[0] and iLeft[-1] < iRight[-1]:
            left, right = iLeft, iRight
        else:
            left, right = iRight, iLeft
        return [left[0], max(left[-1], right[-1])] if left[-1] >= right[0] else None


if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),
        ([[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]], [[2, 4], [5, 5]]),
        ([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]], [[1, 3], [4, 7]])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.merge(t[0])
        tf = res == t[1]
        if not tf:
            sol.merge(t[0])
