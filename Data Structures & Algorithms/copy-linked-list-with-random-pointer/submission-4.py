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
        map = {None : None} # original node : copy
        cur = head
        dummy = Node(0, None, None)
        cpy = dummy

        while cur:
            cpy.next = Node(cur.val, None, None)
            map[cur] = cpy.next
            cpy = cpy.next
            cur = cur.next
        cur2 = head
        cpy2 = dummy.next
        while cur2:
            cpy2.random = map[cur2.random]
            cpy2 = cpy2.next
            cur2 = cur2.next
        return dummy.next



            

        