class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = []

        lp = []
        for i, c in enumerate(s):
            if c == ")":
                if not lp:
                    remove.append(i)
                else:
                    lp.pop()
            elif c == "(":
                lp.append(i)

        skip = remove + lp
        result = ""
        for i, c in enumerate(s):
            if i in skip:
                continue
            result += c
        return result
