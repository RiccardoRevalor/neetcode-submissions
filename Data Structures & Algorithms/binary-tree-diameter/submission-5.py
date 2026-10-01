# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        def depth(node):
            nonlocal maxD
            if not node: return 0
            left = depth(node.left)
            right = depth(node.right)
            maxD = max(maxD, left+right) #5,3,2,4 in example
            return 1 + max(left, right)

        depth(root)

        return maxD

        