class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r) // 2
            #compare nums[m] with nums[r]

            if nums[m] > nums[r]:
                #it means the minimum is in the right prt, so move l
                l = m+1
            elif nums[m] < nums[r]:
                #the minimum is in left part, move r
                #not ot jump nums[m], just set r at m
                r = m
            else:
                #nums[m] = nums[r] because l = r, so m = 2r / 2
                return nums[m]
        