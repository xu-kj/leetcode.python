# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        t = head
        p = None
        while t:
            p = ListNode(t.val, p)
            t = t.next
        return p
