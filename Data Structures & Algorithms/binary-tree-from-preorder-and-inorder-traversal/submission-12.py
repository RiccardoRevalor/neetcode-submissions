# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #pre order: root, left, right
        #in order: left, root, right
        if not preorder: return None
        if not inorder: return None


        inorder_d = {val: i for i, val in enumerate(inorder)} #for O(1) index lookups

        def recur(preorder_start, preorder_end, inorder_start, inorder_end) -> Optional[TreeNode]:
            nonlocal inorder_d

            if preorder_start > preorder_end:
                return None

            #root is 1st node in preorder
            root = TreeNode(preorder[preorder_start])
            #find root in thbe inorder array, so that I can have:
            #in inorder -> left tree | root | right tree
            root_inorder = inorder_d[root.val] - inorder_start #inorder.index(root.val)
            #now recursively apply this to the left subtree and right subtree of root_inorder, found in inorder

            #preorder is root | left subtree | right subtree
            #root_inorder is the size of left subtree
            left_end = root_inorder
            left_size = root_inorder
            right_start = left_end +1
            root.left = recur(preorder_start+1, preorder_start+ left_size, inorder_start, 
            inorder_start + left_size -1)
            root.right = recur(preorder_start+left_size+1, preorder_end, inorder_start+left_size+1, inorder_end)

            return root

        return recur(0, len(preorder)-1, 0, len(inorder)-1)





        