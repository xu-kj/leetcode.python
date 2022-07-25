from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        result = []
        for w in arr:
            if count[w] == 1:
                result.append(w)

        return result[k - 1] if k <= len(result) else ""
