"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        root = Node()
        cloned = {}

        def recur(src, copy):
            #end condition, node already cloned
            if src in cloned: return cloned[src]

            #clone node
            copy.val = src.val
            cloned[src] = copy

        
            #iterate through src' neighbors, clone them and put them in cloned list
            for srcNeigh in src.neighbors:
                copiedNeigh = recur(srcNeigh, Node())
                if copiedNeigh:
                    copy.neighbors.append(copiedNeigh)
            
            return copy

        recur(node, root)
        return root


        