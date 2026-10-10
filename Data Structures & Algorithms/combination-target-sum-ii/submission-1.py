class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        #CAVEAT: Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

        #similar to coin problem
        #go left to right to avoid repeating combinations
        #in coins I used memoization because i needed the number of combinations
        #here, i need to list all conbinations, so i backtrack
        res = []
        nums.sort() 

        def recur(i, temp, amount):
            #good end: amount is zero
            if amount == 0:
                res.append(temp)
                return 
            #bad condition: amount < zero or at the end of array-> backtrack, do not add to solution
            if amount < 0 or i >= len(nums): return

            #2 cases:
            #1: i subtract the amount by nums[i]
            #2: i skip nums[i]

            recur(i+1, temp + [nums[i]], amount - nums[i]) #I CAN USE IT AT MOST ONCE, SO I+1
            #here, i take the value at nums[i], but then i need to make sure i do not creste a duplicate combination with the same value at a different index. this is why i sorted
            j = i+1
            while j < len(nums) and nums[i] == nums[j]: j+=1
            #now j for sure does not point to a number I already used in case 1
            recur(j, temp, amount)
            #if i take the 

        recur(0, [], target)
        return res
        