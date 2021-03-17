from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        c = {}
        l, r = 0, 0
        result = 0
        cur = 0
        while r < len(nums):
            if nums[r] in c:
                result = max(result, cur)
                for _ in range(c[nums[r]] + 1 - l):
                    c.pop(nums[l])
                    cur -= nums[l]
                    l += 1
            c[nums[r]] = r
            cur += nums[r]
            r += 1
        result = max(result, cur)
        return result


if __name__ == "__main__":
    test_cases = [
        ([4, 2, 4, 5, 6], 17),
        ([5, 2, 1, 2, 5, 2, 1, 2, 5], 8)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.maximumUniqueSubarray(t[0])
        tf = res == t[1]
        if not tf:
            sol.maximumUniqueSubarray(t[0])
