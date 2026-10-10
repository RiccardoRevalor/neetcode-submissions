class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] #for sure empty subset
        if len(nums) == 0: return res

        def recur(i, temp):
            if i >= len(nums): 
                res.append(temp) #temp is the subset
                return

            #2 cases:
            #1: add element of index i to subset temp
            #2: do not add it
            recur(i+1, temp) #do not add element at index i
            recur(i+1, temp + [nums[i]]) #add element at index i
            

        recur(0, [])
        return res

        