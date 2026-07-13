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
        dummy = Node(0, None, None)
        copy = dummy
        head2 = head
        map = {} #og : cpy
        while head2:
            newNode = Node(head2.val, None, None)
            copy.next = newNode
            map[head2] = copy.next
            head2 = head2.next
            copy = copy.next
        copy2 = dummy.next
        while head:
            # were getting the random value of the copy here
            if head.random:
                copy2.random = map[head.random]
            else:
                copy2.random = None
            copy2 = copy2.next
            head = head.next
        return dummy.next
