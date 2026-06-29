# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, nxt = None, head
        while nxt:
            tmp = nxt.next
            nxt.next = curr
            curr, nxt = nxt, tmp
        return curr
        