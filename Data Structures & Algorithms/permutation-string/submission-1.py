class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs = defaultdict(int)
        for ch in s1: freqs[ch]+=1

        #now build window
        l = 0
        for r in range(len(s2)):
            ch2 = s2[r]
            #decrease freq, take ch2 into window
            freqs[ch2] -=1

            #if negative, move window
            while freqs[ch2] < 0 and l < len(s2):
                freqs[s2[l]] +=1 #discard first el on the left
                l+=1

            #end condition: size of window is == size of substring
            if r-l+1 == len(s1): return True

        return False
        