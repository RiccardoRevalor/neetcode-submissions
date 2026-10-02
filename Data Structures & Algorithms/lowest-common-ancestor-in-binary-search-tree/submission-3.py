# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def findLCA(node, p, q):
            if node.val < p.val and node.val < q.val:
                #go right
                return findLCA(node.right, p, q)
            elif node.val > p.val and node.val > q.val:
                #go left
                return findLCA(node.left, p, q)
            else:
                return node

        return findLCA(root, p, q)

        