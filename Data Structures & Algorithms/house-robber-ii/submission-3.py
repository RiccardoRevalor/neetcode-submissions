class Solution:
    def rob(self, nums: List[int]) -> int:


        n = len(nums)
        if n == 1: return nums[0]


        def straightline(lo, hi):
            
            memo = {}

            def recursion(i, n):
                
                if i >= n: return 0
                if i in memo:
                    return memo[i]
                else:

                    memo[i] = max(nums[i] + recursion(i+2,n), recursion(i+1,n))

                    return memo[i]
            
            return recursion(lo, hi)

        case1 = straightline(0, n-1)
        case2 = straightline(1,n)
        return max(case1, case2)

        