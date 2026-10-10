class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 0 or n < 0: return None

        memo = {}

        def recur(i, j):
            if i == m -1 and j == n-1: return 1
            if i >= m or j >= n: return 0 #off grid
            
            if (i,j) in memo: return memo[(i,j)]


            result = recur(i+1, j) + recur(i, j+1)

            memo[(i,j)] = result
            return result

        return recur(0,0)
        