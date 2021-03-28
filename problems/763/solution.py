from typing import List
import string


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        intervals = []
        for c in string.ascii_lowercase:
            left = S.find(c)
            right = S.rfind(c)
            if left >= 0 and right >= 0:
                intervals.append([left, right])

        merged_intervals = []
        for interval in sorted(intervals, key=lambda interval: interval[0]):
            if not merged_intervals:
                merged_intervals.append(interval)
                continue

            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1]
                                              [1], interval[1])
            else:
                merged_intervals.append(interval)
        lengths = [interval[1] - interval[0] + 1 for interval in merged_intervals]
        return lengths


if __name__ == "__main__":
    test_cases = [
        ("ababcbacadefegdehijhklij", [9, 7, 8])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.partitionLabels(t[0])
        tf = res == t[1]
        if not tf:
            sol.partitionLabels(t[0])
