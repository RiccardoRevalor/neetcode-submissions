class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #other naive approach: use a prefix style approach
        #at each index 

        #for each index, we need the prod of all elements before the index, and the prod of all elements after the index
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        #pref of 1st el
        pref[0] = 1
        #suff of last el
        suff[-1] = 1

        #res[i] = pref[i] * suff[i]

        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]

        for i in range(n):
            res[i] = suff[i] * pref[i]

        return res

        