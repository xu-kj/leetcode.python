import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        summary = collections.Counter(t)

        filtered_indexes = [i for i in range(len(s)) if s[i] in t]
        result = ""
        l, r = 0, 0
        while l < len(filtered_indexes):
            while r < len(filtered_indexes):
                ri = filtered_indexes[r]
                if s[ri] in summary:
                    summary[s[ri]] -= 1
                r += 1
                if all([c <= 0 for c in summary.values()]):
                    break
            while all([c <= 0 for c in summary.values()]):
                ri = filtered_indexes[r - 1] + 1
                li = filtered_indexes[l]
                if not result or (ri - li) < len(result):
                    result = s[li:ri]
                if s[li] in summary:
                    summary[s[li]] += 1
                l += 1

            if r == len(filtered_indexes):
                break
        return result

if __name__ == "__main__":
    test_cases = [
        ('ADOBECODEBANC', 'ABC', 'BANC'),
        ('a', 'a', 'a'),
        ('aa', 'aa', 'aa'),
        ('bba', 'ab', 'ba'),
        ('ab', 'a', 'a'),
        ('cabwefgewcwaefgcf', 'cae', 'cwae')
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.minWindow(t[0], t[1])
        tf = res == t[2]
        if not tf:
            sol.minWindow(t[0], t[1])
