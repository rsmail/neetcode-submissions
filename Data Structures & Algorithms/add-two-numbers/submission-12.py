# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        cur = dummy

        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1: v1 = l1.val
            if l2: v2 = l2.val
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            cur = cur.next
        return dummy.next
