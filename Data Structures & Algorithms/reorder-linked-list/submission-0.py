# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        head1, head2 = split(head)
        head2 = reverse(head2)
        merge(head1, head2)


def split(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    head1, head2 = head, slow.next
    slow.next = None
    return head1, head2


def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def merge(head1, head2):
    head = ListNode()
    curr = head
    while head1:
        curr.next = head1
        head1 = head1.next
        curr = curr.next
        if head2:
            curr.next = head2
            head2 = head2.next
            curr = curr.next
    return head.next
    
