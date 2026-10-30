# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        accumulator = 0
        while head:
            #case 1: the current node it not 0: add value to accumulator, do not add it yet to res
            if head.val != 0:
                accumulator += head.val

            else:
                #case 2: found a zero
                #if accumulator == 0: we are at beginning, skip
                if accumulator == 0:
                    head = head.next
                    continue

                #add new node to res
                newNode = ListNode(accumulator, None)
                res.next = newNode
                accumulator = 0
                res = res.next

            head = head.next

        return dummy.next
        