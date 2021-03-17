class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        result = 0
        c = {}
        while r < len(s):
            if s[r] in c:
                result = max(result, r - l)
                t = c[s[r]] + 1
                for i in range(l, t):
                    c.pop(s[i])
                l = t
            c[s[r]] = r
            r += 1
        result = max(result, r - l)
        return result


if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("abba", 2)
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.lengthOfLongestSubstring(t[0])
        tf = res == t[1]
        if not tf:
            sol.lengthOfLongestSubstring(t[0])
