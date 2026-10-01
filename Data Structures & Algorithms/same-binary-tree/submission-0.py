# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def check(nodeP, nodeQ):
            #null values
            if nodeP is None and nodeQ is None: return True
            if nodeP is not None and nodeQ is None: return False
            if nodeP is None and nodeQ is not None: return False
            #first check vals
            if nodeP.val != nodeQ.val: return False
            #then check if equivalence holds for the two children
            checkLeft = check(nodeP.left, nodeQ.left)
            checkRight = check(nodeP.right, nodeQ.right)
            return checkLeft and checkRight

        return check(p,q)

        
        