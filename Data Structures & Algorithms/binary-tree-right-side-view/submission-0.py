# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def bfs(node):
            if node is None: return []

            res = [node.val] #root always visible

            queue = deque()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

            while queue:
                count = len(queue)
                chosen = queue[-1] #rightmost
                res.append(chosen.val)

                for i in range(count):
                    popped = queue.popleft()
                    if popped.left: queue.append(popped.left)
                    if popped.right: queue.append(popped.right)

            return res

        return bfs(root)
                    




        