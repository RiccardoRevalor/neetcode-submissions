# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #first, split in half, find the second half, use FAST POINTER, SLOW POINTER
        fast, slow = head.next, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        #second, invert the second half of the list
        #start of 2nd list is slow.next
        current = slow.next
        #cut in half by detatching first half from second
        slow.next = None
        previous = None

        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp


        #third, merge the first half with the reversed second half
        first, second = head, previous


        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            #shift
            first = tmp1
            second = tmp2 


        
        