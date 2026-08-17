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
        #we need to use a map from og nodes to copy nodes, that way we can add in random pointers
        if not head:
            return None
        dummy = Node(0)
        cpy = dummy
        cpy2 = dummy
        map = {None : None}
        head1, head2 = head, head
        while head1:
            cpy.val = head1.val
            map[head1] = cpy
            if head1.next:
                cpy.next = Node(0)
            cpy = cpy.next
            head1 = head1.next
        
        while head2:
            #here head = cpy
            #we want to add in cpy.random
            #so we get map[head2.random]
            cpy2.random = map[head2.random]
            cpy2 = cpy2.next
            head2 = head2.next
        
        return dummy


    
        