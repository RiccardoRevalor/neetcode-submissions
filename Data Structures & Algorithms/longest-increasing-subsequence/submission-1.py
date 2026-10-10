class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0

        memo = {}

        def recur(i):
            #return len of longest increasing subsequent ending in index i

            if i == 0: return 1

            if i in memo: return memo[i]

            result = 1 #because nums[i] itself is a valid subseq, of length 1

            for j in range(i):
                if nums[j] < nums[i]:
                    #two choices, I either add nums[j] to sequence, or not
                    result = max(result,  1 + recur(j)) #here i jump to index j
            
            memo[i] = result
            return memo[i]

        longest = -1
        for i in range(len(nums)):
            max_i = recur(i)
            longest = max(longest, max_i)

        return longest



        