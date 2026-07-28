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
        dummy = Node(0)
        cur = dummy
        og = head
        og2 = head
        map = {None : None}

        while og:
            cur.next = Node(og.val)
            map[og] = cur.next
            og = og.next
            cur = cur.next            
        cur2 = dummy.next
        while og2:
            cur2.random = map[og2.random]
            og2 = og2.next
            cur2 = cur2.next
        return dummy.next
        