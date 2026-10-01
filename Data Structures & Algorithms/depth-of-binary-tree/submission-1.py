# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        if not root: return maxD

        stack = [(root, 1)] #(node, depth)

        while stack:
            tupla = stack.pop()
            node = tupla[0]
            depth = tupla[1]
            maxD = max(maxD, depth)

            if node.left is not None:
                stack.append([node.left, depth+1])
            if node.right is not None:
                stack.append([node.right, depth+1])

        return maxD

            


        