class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #this is different from conbinations because here order matters
        #so, [1,3] != [3,1], aka they are 2 different results
        res = []

        def recur(temp, remaining):
            n = len(remaining)
            if n == 0:
                #found a solution, append it to red and return
                res.append(temp)
                return

            for j in range(n):
                #i iterate through all remaoining elements, and take 1 of themn at each pass,
                #i remove it from remaining and do recurrence
                recur(temp + [remaining[j]], remaining[:j] + remaining[j+1:])

        recur([], nums)

        return res
        