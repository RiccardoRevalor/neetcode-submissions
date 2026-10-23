class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        best = 0

        memo = {} #key: index (i1, i2), val: len common subseq possible from index i

        def recur(i1, i2):
            #end
            if i1 >= len(text1) or i2 >= len(text2): return 0

            if (i1, i2) in memo: return memo[(i1, i2)]

            #if ch match, add it to subseq
            ch1 = text1[i1]
            ch2 = text2[i2]
            
            if ch1 == ch2:
                res = 1+recur(i1+1, i2+1)
            else:
                res = max(recur(i1+1, i2), recur(i1, i2+1))

            memo[(i1, i2)] = res
            return res

        return recur(0, 0)


        