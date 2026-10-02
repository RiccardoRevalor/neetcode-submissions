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

        if not head: return None

        #orig = {} #key: randomly pointed original node, value: original node that points to it
        copied = {} #key: original node, value: its COPY
        waiting = {} #key: original target, value: list of copies that wanna point at the copy of the original target

        def deepcopy(node, prev, source):
            if source is None: 
                #end of the list
                return 
            node.val = source.val
            #put into orig
            if source.random:
                if source.random not in copied.keys():
                    #it means have not yet ecnountered the pointed node
                    if source.random in waiting:
                        waiting[source.random].append(node)
                    else:
                        waiting[source.random] = [node]
                else:
                    #BACKWARD RANDOM LINK FROM CURRENT NODE BEING COPIED TO A NODE ALREADY COPIED
                    #add the link in the copied list as well
                    node.random = copied[source.random]

            
            #if the source is the target for already other copied nodes, 
            #now it is time to set those links
            if source in waiting:
                for copiedNode in waiting.pop(source):
                    #FORWARD RANDOM LINK FROM A NODE ALREADY COPIED TO CURRENT NODE BEING COPIED
                    copiedNode.random = node

            #save the mapping between orig and copy
            copied[source] = node


            if prev: prev.next = node
            deepcopy(Node(0), node, source.next)

        
        newHead = Node(0)
        deepcopy(newHead, None, head)



        return newHead

        

        


            
        