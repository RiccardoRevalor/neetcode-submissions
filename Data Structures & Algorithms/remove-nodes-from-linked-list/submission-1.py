# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #very bruteforce
        res = ListNode(next = head)
        res2 = res

        while head and head.next: #no point in checking last node
            j = head
            thresh = head.val
            remove = False
            while j and not remove:
                if j.val > thresh:
                    remove = True
                j = j.next

            if remove:
                #remove node from res
                res2.next = head.next
            else:
                res2 = res2.next #only advance res2 when we keep a node
            head = head.next

        return res.next


        