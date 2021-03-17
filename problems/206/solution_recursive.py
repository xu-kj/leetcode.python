# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        t = self.reverseList(head.next)
        if not t:
            return head

        # head.next becomes the last element of the reversed linked list
        head.next.next = head
        head.next = None
        return t
