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
        #traverse once and create a new list of copies...
        #also create a dict that maps the original to the copy
        map = {} #og : copy
        dummy = Node(0, None, None)
        copy = dummy
        head2 = head

        while head2:
            
            newNode = Node(head2.val, None, None)
            copy.next = newNode
            map[head2] = copy.next
            head2 = head2.next
            copy = copy.next
        
        copy2 = dummy.next
        while copy2: # here we are traversing both because they are the same size
        #we need to use the dict to map the original.random to the copy.random nodes
        # how to do that: get map[og.random] = the cpy random node
            if head.random:
                copy2.random = map[head.random]
            else:
                copy2.random = None
            copy2 = copy2.next
            head = head.next
        return dummy.next
            
        
