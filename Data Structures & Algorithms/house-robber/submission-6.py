class Solution:
    def rob(self, nums: List[int]) -> int:


        memo = {}
        n = len(nums)

        def recursion(i, n):
            nonlocal memo
            if i >= n: return 0
            if i in memo:
                return memo[i]
            else:

                memo[i] = max(nums[i] + recursion(i+2,n), recursion(i+1,n))

                return memo[i]

        return recursion(0, n)

        