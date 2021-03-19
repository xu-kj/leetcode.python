from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_window_sum = 0

        r = k - 1
        window_sum = 0
        for l in range(r, r - 2 * k, -1):
            window_sum += cardPoints[l]
            if r - l >= k:
                window_sum -= cardPoints[r]
                r -= 1
            if r - l == k - 1:
                max_window_sum = max(max_window_sum, window_sum)
        return max_window_sum


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 1], 3, 12),
        ([2, 2, 2], 2, 4),
        ([9, 7, 7, 9, 7, 7, 9], 7, 55),
        ([1, 1000, 1], 1, 1),
        ([1, 79, 80, 1, 1, 1, 200, 1], 3, 202)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.maxScore(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.maxScore(t[0], t[1])
