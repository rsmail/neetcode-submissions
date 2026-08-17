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
        map = {None : None}
        dummy = Node(0)
        head1, head2 = head, head
        cur1, cur2 = dummy, dummy
        while head1:
            cur1.next = Node(head1.val)
            map[head1] = cur1.next
            head1 = head1.next
            cur1 = cur1.next
        
        while head2:
            cur2.next.random = map[head2.random]
            cur2 = cur2.next
            head2 = head2.next
        return dummy.next

        