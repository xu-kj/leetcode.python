from typing import *


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = ""
        rm = len(ls)
        for c in s:
            if c not in ls:
                ls += c
                rm = max(rm, len(ls))
            else:
                ls = ls[ls.index(c) + 1:] + c
                # rm = max(rm, len(ls))
        return rm


if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.lengthOfLongestSubstring(t[0])
        tf = res == t[1]
        if not tf:
            sol.lengthOfLongestSubstring(t[0])
