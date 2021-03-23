from typing import List
import collections
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set([word for word in wordList if word != beginWord])
        if endWord not in words:
            return 0

        q = collections.deque([])
        next_q = collections.deque([beginWord])
        steps = 0
        while next_q and not q:
            q = next_q.copy()
            next_q.clear()
            steps += 1

            while q:
                curr = q.popleft()
                for i in range(len(curr)):
                    for c in string.ascii_lowercase:
                        t = curr[:i] + c + curr[i + 1:]
                        if t == endWord:
                            return steps + 1
                        elif t in words:
                            next_q.append(t)
                            words.remove(t)
        return 0


if __name__ == "__main__":
    test_cases = [
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            5
        ),
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log"],
            0
        )
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.ladderLength(t[0], t[1], t[2])
        if res != t[3]:
            sol.ladderLength(t[0], t[1], t[2])
