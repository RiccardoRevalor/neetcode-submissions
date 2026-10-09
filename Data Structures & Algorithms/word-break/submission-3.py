class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #solution with bottom up DP
        n = len(s)
        dp = [False] * (n+1) #this is f(i) in topdown approach
        dp[n] = True

        #the loop models the recursion in topdown approach
        #but in th opposite direction
        #in top down we went low -> high
        #so here we go high -> low
        for i in range(n-1, -1, -1):
            #same content of top down
            #but here we iterate low -> high
            amount = s[i:]
            for word in wordDict:
                #s at index i ONWARD starts with word? so low -> high
                #opposite of top down 
                if amount.startswith(word) and dp[i+ len(word)]:
                    dp[i] = True 
                    break #sol found, early exit
        
        #now at the end, if i continue to iterate, i'll arrive at very first char.
        return dp[0]


        
