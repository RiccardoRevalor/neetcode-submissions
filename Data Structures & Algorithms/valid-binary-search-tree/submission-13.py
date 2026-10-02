# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node):
            if node is None: return False
            queue = deque([(node, float('-inf'), float('inf'))])


            while queue:
                n, min_, max_ = queue.popleft()
                
                #if n is None: return False
                if not (min_ < n.val < max_): return False
                if n.left: queue.append((n.left, min_, n.val))
                if n.right: queue.append((n.right, n.val, max_))
            return True

        return check(root) 
        