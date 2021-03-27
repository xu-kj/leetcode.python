from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        right = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
                continue
            if interval[0] > newInterval[1]:
                right.append(interval)
                continue

            newInterval[0] = min(newInterval[0], interval[0])
            newInterval[1] = max(newInterval[1], interval[1])

        return left + [newInterval] + right


if __name__ == "__main__":
    test_cases = [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
         [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([], [5, 7], [[5, 7]]),
        ([[1, 5]], [2, 3], [[1, 5]]),
        ([[1, 5]], [2, 7], [[1, 7]])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.insert(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.insert(t[0], t[1])
