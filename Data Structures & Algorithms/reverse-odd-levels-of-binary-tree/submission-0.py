# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #bfs + swapping
        queue = deque([root])

        level = 0 #at odd levels we swap

        while queue:
            if level % 2 != 0:
                #swap
                #use 2 pointers for swapping
                #swap vals not the pointers left/right
                l = 0 
                r = len(queue)-1
                while l < r:
                    queue[l].val, queue[r].val = queue[r].val, queue[l].val

                    l+=1
                    r-=1
            
            #do bfs per level
            for l in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            level +=1

        return root

        