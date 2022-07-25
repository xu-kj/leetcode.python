from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = {}
        for w in words1:
            if w in count:
                count[w][0] += 1
            else:
                count[w] = [1, 0]
        for w in words2:
            if w in count:
                count[w][1] += 1
            else:
                count[w] = [0, 1]

        result = 0
        for w, c in count.items():
            if c[0] == 1 and c[1] == 1:
                result += 1

        return result
