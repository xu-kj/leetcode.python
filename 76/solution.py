import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        summary = collections.Counter(t)

        result = ""
        l, r = 0, 0
        while l < len(s):
            while r < len(s):
                if s[r] in summary:
                    summary[s[r]] -= 1
                r += 1
                if all([c <= 0 for c in summary.values()]):
                    break
            while all([c <= 0 for c in summary.values()]):
                if not result or (r - l) < len(result):
                    result = s[l:r]
                if s[l] in summary:
                    summary[s[l]] += 1
                l += 1

            if r == len(s):
                break
        return result

if __name__ == "__main__":
    test_cases = [
        ('ADOBECODEBANC', 'ABC', 'BANC'),
        ('a', 'a', 'a'),
        ('aa', 'aa', 'aa'),
        ('bba', 'ab', 'ba')
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.minWindow(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.minWindow(t[0], t[1])
