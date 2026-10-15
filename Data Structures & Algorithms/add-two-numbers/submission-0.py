# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy
        carry = 0

        #loop as long as l1 has elements left, or l2 has elements left, or e have a carry
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else: v1 = 0

            if l2:
                v2 = l2.val
            else: v2 = 0

            total = v1 + v2 + carry
            carry = total // 10
            total = total % 10

            #update node
            tail.next = ListNode(total)

            tail = tail.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next

        