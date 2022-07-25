from math import inf
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        good_for = [1, 7, 30]

        mem = [
            [
                [
                    inf for i in range(len(days) + 1)
                ] for j in range(len(days))
            ] for k in range(len(costs))
        ]
        for i, cost in enumerate(costs):
            for j in range(len(days)):
                for k in range(j, len(days) + 1):
                    if i == 0:
                        mem[i][j][k] = 0
                        last = -inf
                        for kk in range(j, k):
                            choice = days[kk]
                            if choice >= last + good_for[i]:
                                last = choice
                                mem[i][j][k] += cost
                        continue

                    mem[i][j][k] = mem[i - 1][j][k]
                    for kk in range(j, k).__reversed__():
                        cc = min(cost, mem[i - 1][kk][k])
                        mem[i][j][k] = min(mem[i][j][k], mem[i][j][kk] + cc)

                        if days[kk - 1] <= days[k - 1] - good_for[i]:
                            break

                if i == len(costs) - 1:
                    break

        return mem[-1][0][-1]
