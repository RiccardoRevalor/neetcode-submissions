class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        largest = nums[0]
        curSum = nums[0]

        for i in range(1, len(nums)):
            #at for each element, see if we can improve largest, or not
            #so we can either continue the subarray, byt putting the ne ele,ent into it
            #or break the previous subarray, record the sum, and start a new one
            el = nums[i]
            if curSum + el > el:
                curSum += el
            else: curSum = el
                
            largest = max(largest, curSum)
        
        return largest






        