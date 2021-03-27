from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        for interval in sorted_intervals:
            if not result:
                result.append(interval)
                continue

            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result


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
