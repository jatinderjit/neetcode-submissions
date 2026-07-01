"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        copies = defaultdict(lambda: Node(0))
        copies[None] = None
        node = head
        copy = Node(0)
        while node:
            copy.next = copies[node]
            copy = copy.next
            copy.val = node.val
            copy.random = copies[node.random]
            node = node.next
        return copies[head]