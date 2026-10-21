class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #i suppose Treenode has def __init__(val, left, right) where left, right are other tree nodes
        def buildBST(l, r):
            #at each iteration i have to take the middle element of the subarray, it becomes the root
            #termination
            #if l == r i attach the final leaf node
            #if l > r terminate
            if l > r: return
            mid = (l+r) // 2 #new root of subtree
            #then attach left branch and right branch
            return TreeNode(nums[mid], buildBST(l, mid-1), buildBST(mid+1,r))

        return buildBST(0, len(nums)-1)
