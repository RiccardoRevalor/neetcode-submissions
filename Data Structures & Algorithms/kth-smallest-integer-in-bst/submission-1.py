# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #simpler solution: just in order traversal + array in which i append nodes
        visited = [] #i visit in order, so then i can fastly retrieve the kth smaller el, which will be at index k

        def dfs(node):
            if node == None: return 

            #in order
            dfs(node.left)
            visited.append(node.val)
            dfs(node.right)

        dfs(root)
        return visited[k-1]