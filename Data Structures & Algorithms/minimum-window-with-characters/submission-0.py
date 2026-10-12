class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs = defaultdict(int)
        for ch in t: freqs[ch] +=1

        missing = len(t)
        
        l = 0
        best_l = l
        best_len = float('inf')

        for r in range(len(s)):
            ch2 = s[r]

            #decrement count
            #if count is >= 0 it means thet we actually need that character
            #if it is < 0 it means that character is not in t
            freqs[ch2] -= 1
            if freqs[ch2] >= 0:
                missing -=1

            #at a certain point i reach missing == 0, so i have all needec characters in my sliding window
            #in this case, try to see if i can shorten it
            #from left, because for sure the last character (1st in right) is needed
            while missing == 0:
                len_window = r+1-l
                if len_window < best_len:
                    best_len = len_window
                    best_l = l

                #drop from left, check if it it needed
                freqs[s[l]] +=1
                if freqs[s[l]] > 0:
                    missing +=1
                
                l+=1
        
        if best_len == float('inf'): return ""
        return s[best_l:best_l + best_len]



        
        
        
        