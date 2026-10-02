# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #naive
        l = []
        tail = head
        n = 0
        while tail:
            l.append(tail)
            tail = tail.next

        l2 = []

        for i in range(len(l)):
            if i % 2 == 0:
                #even, select from left
                l2.append(l[i // 2])

            else:
                l2.append(l[n - 1 - i //2])

        for i in range(len(l2)-1):
            l2[i].next = l2[i+1]
        
        l2[-1].next = None

        head = l2[0]




        

        