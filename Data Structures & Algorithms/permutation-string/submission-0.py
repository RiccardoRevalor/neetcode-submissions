class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #1. count all letters in s1
        freqs = defaultdict(int)
        for ch in s1: freqs[ch] +=1

        l=0
        for r in range(len(s2)):
            ch = s2[r]
            #decrease count of ch from budget
            freqs[ch]-=1
            #if negative, move sliding window
            while freqs[ch] < 0 and l < len(s2):
                freqs[s2[l]]+=1 #because i get rid of element at index l, i have to restore its freq
                l+=1

            #check if i found it
            if len(s1) == r-l+1: return True

        return False
        