from typing import List, Set

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        group = [0] * n
        groups = {}
        c = 0
        for connection in connections:
            src, dst = connection[0], connection[1]
            if (not group[src]) and (not group[dst]):
                new_group = c + 1
                c += 1
                groups[new_group] = {src, dst}
                group[src] = new_group
                group[dst] = new_group
            elif not group[src]:
                group[src] = group[dst]
                groups[group[dst]].add(src)
            elif not group[dst]:
                group[dst] = group[src]
                groups[group[src]].add(dst)
            elif group[src] != group[dst]:
                s = min(group[src], group[dst])
                l = max(group[src], group[dst])
                groups[s] |= groups[l]
                for i in groups[l]:
                    group[i] = s
                groups.pop(l, None)
        connection_groups = len(groups.keys())
        for i in range(n):
            if not group[i]:
                connection_groups += 1
        return connection_groups - 1


# if __name__ == "__main__":
    # test_cases = [
    #     (4, [[0,1],[0,2],[1,2]], 1),
    #     (6, [[0,1],[0,2],[0,3],[1,2],[1,3]], 2),
    #     (6, [[0,1],[0,2],[0,3],[1,2]], -1),
    #     (5, [[0,1],[0,2],[3,4],[2,3]], 0)
    # ]
