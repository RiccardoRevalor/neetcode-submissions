class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r) // 2
            #when we split, at least one half is fully sorted

            #so first we find what half is sorted, then it's O(1) (a comparison) to say if target is in sorted half
            if nums[m] == target: return m

            #check if left half is sorted
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    #look left
                    r = m-1
                else:
                    #look right
                    l = m+1
                
            #check if right half is sorted
            else:
                if target > nums[m] and target <= nums[r]:
                    #look right
                    l = m+1
                else:
                    #look left
                    r = m-1
        
        return -1



        
        