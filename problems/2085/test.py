from v1 import Solution

test_cases = [
    (
        ["leetcode", "is", "amazing", "as", "is"], [
            "amazing", "leetcode", "is"],
        2
    ),
    (
        ["b", "bb", "bbb"], ["a", "aa", "aaa"],
        0
    ),
    (
        ["a", "ab"], ["a", "a", "a", "ab"],
        1
    ),
]

for w1, w2, expected in test_cases:
    res = Solution().countWords(w1, w2)
    if res != expected:
        Solution().countWords(w1, w2)
