class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return None
        if len(nums) == 1: return nums[0]
        memo = {} #key: index, value: tuple of (max, min) prod of arrays ending at index i
        
        def recur(i):
            # RETURNS (max, min) product of a subarray that ENDS at index i
            
            if i == 0:
                #1st element
                return nums[i], nums[i]

            if i in memo: return memo[i]

            #at this step I can either start a new array
            #which just has nums[i]
            #or extend a previous array, adding nums[i] to it
            prev_max, prev_min = recur(i-1)

            #case 1: start new array
            x = nums[i]

            #case2: continue previous vrray, 2 subcases: 
            #subcase 1: prev_max * x is positive and highest
            #subcase: prev_min *x turns positive and highest
            case2_1 = prev_max * x
            case2_2 = prev_min * x

            memo[i] = (max(x, case2_1, case2_2), min(x, case2_1, case2_2))
            return memo[i]

        best = -1e9
        for i in range(len(nums)):
            tup = recur(i) #(max prod of sub ending at i, min prod of sub ending at i)
            best_i = max(tup[0], tup[1])
            if best_i > best: best = best_i
        
        return best

        




        