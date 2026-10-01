# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def visitNode(node):
            if not node: return 
            visitNode(node.left)
            res.append(node.val)
            visitNode(node.right)

        visitNode(root)

        return res

        