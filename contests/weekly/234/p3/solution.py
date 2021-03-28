from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kv = {}
        for pair in knowledge:
            kv[pair[0]] = pair[1]

        result = ""
        n = 0
        while n < len(s):
            if s[n] != "(":
                result += s[n]
            else:
                n += 1
                temp = ""
                while s[n] != ")":
                    temp += s[n]
                    n += 1
                result += kv[temp] if temp in kv else "?"
                temp = ""

            n += 1
        return result


if __name__ == "__main__":
    test_cases = [
        ("(name)is(age)yearsold", [["name", "bob"],
         ["age", "two"]], "bobistwoyearsold"),
        ("hi(name)", [["a", "b"]], "hi?"),
        ("(a)(a)(a)aaa", [["a", "yes"]], "yesyesyesaaa"),
        ("(a)(b)", [["a", "b"], ["b", "a"]], "ba")
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.evaluate(t[0], t[1])
        if res != t[2]:
            sol.evaluate(t[0], t[1])
