# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if node is None: return 0
            hLeft = height(node.left)
            hRight = height(node.right)
            return 1 + max(hLeft, hRight)

        def check(node):
            if node is None: return True
            hLeft = height(node.left)
            hRight = height(node.right)
            if abs(hLeft - hRight) > 1: return False
            return check(node.left) and check(node.right)

        return check(root)
            
        