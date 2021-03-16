from typing import *


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s at least contains a palindrome of length 1
        mid_points, pspan = list(range(len(s))), 1

        pspan += 1
        mid_points = [ for mp in mid_points]

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1] and len(substr) > len(maxlen):
                    maxlen = substr
        return maxlen


if __name__ == "__main__":
    test_cases = [
        ('babad', ['bab', 'aba']),
        ('cbbd', ['bb']),
        ('a', ['a'])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.longestPalindrome(t[0])
        tf = res in t[1]
        if not tf:
            sol.longestPalindrome(t[0])
