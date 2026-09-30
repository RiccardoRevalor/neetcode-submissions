class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        res = []

        for i in range(0, n -2):
            if i > 0 and nums[i] == nums[i-1]: continue
            #2 pointers for each i
            j = i+1
            k = n-1
            while j < k:
                psum = nums[i]+nums[j]+nums[k]
                if psum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:j+=1
                elif psum < 0:
                    j +=1
                elif psum > 0:
                    k -=1
        return res


