# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxSoFar):
            if node is None: return 0
            #for each partial path, compare current node with maxSoFar
            res = 0
            if node.val >= maxSoFar:
                res += 1
                maxSoFar = node.val

            #count if there are other good nodes in downstream
            if node.left: 
                res += dfs(node.left, maxSoFar)
            if node.right:
                res += dfs(node.right, maxSoFar)

            return res

        return dfs(root, root.val)


        