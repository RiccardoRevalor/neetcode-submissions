class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sol with sliding window, much more efficient
        #sliding window is valid if len(window) - freq(most frequent letter) <= k
        #if it is not valid, i shift the start
        #each time i expand it to the right
        freqs = defaultdict(int)
        l = 0 #sliding window starts at 0
        best = 0

        #at each iteration i expand r
        for r in range(len(s)):
            #update freqs
            ch = s[r] #new char in window
            freqs[ch] += 1
            len_window = r -l +1
            most_freq = max(freqs.values())
            while len_window - most_freq > k and l < r: 
                #shift window from the left
                freqs[s[l]] -=1
                l+=1
                len_window = r -l +1
            best = max(best, r-l+1)
        
        return best