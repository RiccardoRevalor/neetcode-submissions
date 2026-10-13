class Solution:
    def jump(self, nums: List[int]) -> int:
        #solution witb DFS and memoization
        n = len(nums)
        memo = {}

        def dfs(i):
            #i is the index at which i am at
            #good ending:
            if i >= n -1: 
                return 0 #0 more jumps needed

            if i in memo: return memo[i]

            #try all possible combinations and save min from here in memo
            res = float('inf')
            for j in range(1, nums[i]+1):
                res = min(res, 1 + dfs(i+j))

            memo[i] = res
            return res

        return dfs(0)

        


        