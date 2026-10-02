# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        previous = None
        current = head

        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp

        #no previous is the head of the inverted list
        counter = 1
        #linear time, loop through nodes, delete the nth

        head = node = previous
        print(head.val)

        if n == 1:
            node = node.next #head is gone
            head = head.next
        while node and node.next:
            if counter == n -1:
                #delete next node
                tmp = node.next.next
                node.next = tmp
            node = node.next
            counter +=1


        #now revert the list again
        previous = None
        current = head

        while current:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp


        return previous




            


        