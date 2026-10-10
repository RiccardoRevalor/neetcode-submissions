class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n < 2: return False
        #retrieve sum of all el
        sum = 0
        for el in nums: sum += el

        if sum % 2 != 0: return False

        memo = {}
        target = sum / 2

        def recur(amount, i):
            #can the subset nums[i:] sum to amount?
            #end condition, i used all the amount
            if amount == 0: return True
            if i >= n or amount < 0: return False
            if (amount, i) in memo: return memo[(amount, i)]

            #two choices:
            #1: add nums[i] to my subset, take it
            #2: skip it and focus on nums[i+1]
            result = recur(amount - nums[i], i+1) or recur(amount, i+1)

            memo[(amount, i)] = result
            return result

        return recur(target, 0)

        
        