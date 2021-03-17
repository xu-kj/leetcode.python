from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = deque()
        for i, num in enumerate(nums):
            while window and num > nums[window[-1]]:
                window.pop()
            window.append(i)
            if window[0] <= i - k:
                window.popleft()
            if i >= k - 1:
                results.append(nums[window[0]])
        return results


if __name__ == "__main__":
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.maxSlidingWindow(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.maxSlidingWindow(t[0], t[1])
