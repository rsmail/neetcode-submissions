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
        head2 = head
        mapOgToCopy = {None: None} # og : copy
        dummy = Node(0, None, None)
        cur = dummy

        while head:
            cur.next = Node(head.val, None, None)
            mapOgToCopy[head] = cur.next
            head = head.next
            cur = cur.next

        
        cur2 = dummy.next
        while cur2:
            cur2.random = mapOgToCopy[head2.random]
            cur2 = cur2.next
            head2 = head2.next

        return dummy.next
            


        