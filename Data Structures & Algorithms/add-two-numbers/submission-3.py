# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #first we need to find the longer one...
        #find len of l1
        l1Len = 0
        l12 = l1
        while l12:
            l1Len += 1
            l12 = l12.next
        l2Len = 0
        l22 = l2
        while l22:
            l2Len += 1
            l22 = l22.next
        
        if l2Len > l1Len:
            tmp = l1
            l1 = l2
            l2 = tmp

        res = ListNode(0, None)
        res1 = res
        switch = False
        while l1:
            val = 0
            if switch:
                val += 1
                switch = False
            if l2:
                val += l1.val + l2.val
                if val > 9:
                    switch = True
                    val = val - 10
                node = ListNode(val, None)
                res.next = node
                l1 = l1.next
                l2 = l2.next
                res = res.next
            else:
                val += l1.val
                if val > 9:
                    val -= 10
                    switch = True
                node = ListNode(val, None)
                res.next = node
                l1 = l1.next
                res = res.next

                    

        if switch:
            res.next = ListNode(1, None)
        return res1.next


            

        
