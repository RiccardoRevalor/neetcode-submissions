class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #similar to coin problem
        #go left to right to avoid repeating combinations
        #in coins I used memoization because i needed the number of combinations
        #here, i need to list all conbinations, so i backtrack
        res = []

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

            recur(i, temp + [nums[i]], amount - nums[i]) #I CAN USE THE NUMBER AS MANY TIMES AS I LIKE, SO HERE I STAY AT I
            recur(i+1, temp, amount)

        recur(0, [], target)
        return res
        