from typing import *


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(numbers: List[int]):
        if numbers:
            r = ListNode(numbers[0])
            r.next = ListNode.create(numbers[1:])
            return r
        return None

    def expand(self):
        r = [self.val]
        if (self.next):
            r.extend(self.next.expand())
        return r


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = l1
        while l1:
            if l2:
                l1.val += l2.val
                l2 = l2.next
            if l1.next:
                l1.next.val += l1.val // 10
            # elif l1.val >= 10 or l2:
            elif l1.val >= 10:
                l1.next = ListNode(l1.val // 10)

            l1.val %= 10
            l1 = l1.next
        return r


if __name__ == "__main__":
    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([4], [5], [9]),
        ([0], [7, 3], [7, 3])
    ]

    sol = Solution()
    for t in test_cases:
        res = sol.addTwoNumbers(ListNode.create(t[0]), ListNode.create(t[1]))
        tf = res.expand() == t[2]
        if not tf:
            sol.addTwoNumbers(ListNode.create(t[0]), ListNode.create(t[1]))
