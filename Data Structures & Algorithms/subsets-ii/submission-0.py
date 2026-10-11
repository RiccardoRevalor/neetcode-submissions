class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums: return res
        n = len(nums)
        #sort nums,, why? because i need to remove duplicate subsets
        #so by sorting, when i add a number, i can iterate my pointer to exclude forther nunbers that are the same
        nums.sort()

        def recur(temp, i):
            if i == n: 
                #i completed one subset
                #add to res and return
                res.append(temp)
                return

            #2 cases
            #1: i add the element at index i
            #but in this case then i need to avoid adding again the same number
            #2: i skip it

            #case 1
            recur(temp + [nums[i]], i+1) #i+1 because i cannot use the same element again anymore
            #here, make sure that i skipp also all elements == nums[i]
            j = i+1
            while j < n and nums[j] == nums[i]: j+=1

            #case 2: skip it 
            recur(temp, j)

        recur([], 0)
        return res
            
        