from v1 import Solution

test_cases = [
    (
        ["d", "b", "c", "b", "c", "a"], 2,
        "a"
    ),
    (
        ["aaa", "aa", "a"], 1,
        "aaa"
    ),
    (
        ["a", "b", "a"], 3,
        ""
    ),
]

for arr, k, expected in test_cases:
    res = Solution().kthDistinct(arr, k)
    if res != expected:
        Solution().kthDistinct(arr, k)
