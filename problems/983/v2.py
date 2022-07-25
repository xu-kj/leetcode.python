from math import inf
from typing import List

# dp[i] = min(cost[j] + dp[p]), where days[p] >= days[i] + good_For[j]
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        good_for = [1, 7, 30]

        mem = [inf for i in range(len(days))]

        for i in range(len(days)).__reversed__():
            for j, cost in enumerate(costs):
                c = cost
                for ii in range(i, len(days)):
                    if days[ii] - days[i] >= good_for[j]:
                        c += mem[ii]
                        break
                mem[i] = min(mem[i], c)

        return mem[0]
