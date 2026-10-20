class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #two pointer approach
        i,j = 0,0
        #i: iterates through s, j iterates through s
        for i in range(len(s)):
            if s[i] == t[j]:
                #j-th ch matched
                j+=1

            if j == len(t): return 0


        #now j is the count of matched characters
        return len(t)-j

            
        