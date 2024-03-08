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
