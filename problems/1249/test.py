from v1 import Solution

test_cases = [
    (
        "lee(t(c)o)de)", "lee(t(c)o)de"
    ),
    (
        "a)b(c)d", "ab(c)d"
    ),
    (
        "))((", ""
    ),
]

for input, output in test_cases:
    sol = Solution()
    res = sol.minRemoveToMakeValid(input)
    if res != output:
        sol.minRemoveToMakeValid(input)
