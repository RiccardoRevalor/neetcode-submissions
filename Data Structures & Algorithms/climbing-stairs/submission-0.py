class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {} #key: index i (position), val: way of climving to theb top from i

        def recur(i):
            #i = position
            #end: reach n -> this way is valid
            if i == n: return 1
            if i > n: return 0

            if i in memo: return memo[i]

            #at each step we can either climb 1 or 2 steps
            res = recur(i+1)+recur(i+2)

            memo[i] = res

            return res

        return recur(0)
        