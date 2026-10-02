# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #solution with two pointers algo + dummy node
        dummy = ListNode(0, head)
        left = dummy
        #right pointer at head + n
        right = head
        for i in range(n): right = right.next

        #keep going until right is none
        while right:
            right = right.next
            left = left.next

        #hen right reached end of list, it means left is athe the ndoe before the one we wanna eliminate
        jump = left.next.next
        left.next = jump

        return dummy.next
