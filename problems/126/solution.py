from typing import List, Dict
import collections
import string


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set([word for word in wordList if word != beginWord])
        if endWord not in words:
            return []

        parents = {}
        results = []

        def buildLadders(start: str, ladder: List[str]) -> None:
            if start == beginWord:
                results.append(ladder)
                return

            for parent in parents[start]:
                buildLadders(parent, [parent] + ladder)

        q = []
        next_q = set([beginWord])
        while next_q and not q and endWord not in parents:
            q = collections.deque(next_q)
            next_q.clear()

            while q:
                curr = q.popleft()
                for i in range(len(curr)):
                    for c in string.ascii_lowercase:
                        t = curr[:i] + c + curr[i + 1:]
                        if t in words:
                            next_q.add(t)
                            if t in parents:
                                parents[t].append(curr)
                            else:
                                parents[t] = [curr]
            for word in next_q:
                words.remove(word)
        if endWord in parents:
            buildLadders(endWord, [endWord])
        return results


if __name__ == "__main__":
    test_cases = [
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log", "cog"],
            [
                ["hit", "hot", "dot", "dog", "cog"],
                ["hit", "hot", "lot", "log", "cog"]
            ]
        ),
        (
            "hit",
            "cog",
            ["hot", "dot", "dog", "lot", "log"],
            []
        ),
        (
            "hot",
            "dog",
            ["hot", "dog"],
            []
        )
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.findLadders(t[0], t[1], t[2])
        if len(res) != len(t[3]):
            sol.findLadders(t[0], t[1], t[2])
