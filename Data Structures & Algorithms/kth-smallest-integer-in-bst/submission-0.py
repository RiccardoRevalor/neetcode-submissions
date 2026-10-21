# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #DFS with in order traversal
        d = {} #key: kth smallest element, val: val of node

        def dfs(node, before):
            #before: number of nodes visited before this subtree
            
            #in order

            if node == None: return 0

            left_size = dfs(node.left, before)

            #compute position of node
            pos = before + left_size +1

            d[pos] = node.val

            right_size = dfs(node.right, pos)

            return left_size + right_size +1

        dfs(root, 0)
        return d[k]



            

        