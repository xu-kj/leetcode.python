from typing import *


class Node:
    def __init__(self):
        self.outward = set()
        self.inward = 0


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        nodes = {}
        for i in range(min(1, len(words))):
            for c in words[i]:
                if c not in nodes:
                    nodes[c] = Node()
        for i in range(len(words) - 1):
            for c in words[i + 1]:
                if c not in nodes:
                    nodes[c] = Node()

            order = self.getOrder(words[i], words[i+1])
            if order and order[-1] not in nodes[order[0]].outward:
                nodes[order[0]].outward.add(order[1])
                nodes[order[-1]].inward += 1

        result = ""
        for k in nodes:
            if nodes[k].inward == 0 and len(nodes[k].outward) == 0:
                result += k
        for c in result:
            nodes.pop(c)
        while len(nodes):
            cur = None
            for k in nodes:
                if nodes[k].inward == 0:
                    cur = k
                    break
            if cur is None and len(nodes) != 0:
                return ""
            result += cur
            node = nodes.pop(cur)
            for o in node.outward:
                if o not in nodes:
                    return ""
                nodes[o].inward -= 1
        return result

    def getOrder(self, w1: str, w2: str) -> List[str]:
        l = min(len(w1), len(w2))
        for i in range(l):
            if w1[i] != w2[i]:
                return [w1[i], w2[i]]
        return None


if __name__ == "__main__":
    test_cases = [
        (
            [
                "wrt",
                "wrf",
                "er",
                "ett",
                "rftt",
            ], "wertf"
        ),
        (
            [
                "z",
                "z",
            ], "z"
        ),
        (
            [
                "zy",
                "zx",
            ], "yxz"
        ),
        (
            [
                "ac",
                "ab",
                "b"
            ], "acb"
        ),
        (
            [
                "za",
                "zb",
                "ca",
                "cb",
            ], "abzc"
        ),
        (
            [
                "wnlb",
            ], "wnlb"
        )
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.alienOrder(t[0])
        if res != t[1]:
            sol.alienOrder(t[0])
