from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        r = []
        while head is not None:
            r.append(head)
            head = head.next

        r.sort(key=lambda n: n.val)
        for i in range(len(r)):
            if i+1 == len(r):
                r[i].next = None
            else:
                r[i].next = r[i+1]
        return None if len(r) == 0 else r[0]


# if __name__ == "__main__":
    # test_cases = [
    #     ([2, 7, 11, 15], 9, [1, 2]),
    #     ([0, 0, 3, 4], 0, [1, 2]),
    #     ([5, 25, 75], 100, [2, 3]),
    #     ([3, 24, 50, 79, 88, 150, 345], 200, [3, 6])
    # ]

    # sol = Solution()
    # for t in test_cases:
    #     res = sol.twoSum(t[0], t[1])
    #     tf = res == t[2]
    #     if not tf:
    #         sol.twoSum(t[0], t[1])
