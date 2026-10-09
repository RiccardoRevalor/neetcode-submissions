class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith("0"): return 0
        counter = 0
        memo = {} #memoization

        def recursion(start):
            if start >= len(s): #we reached the end
                return 1 #1 more valid way of decoding the string
            #non numeric characters, invalid
            char_ = s[start]
            if not char_.isdigit(): return 0
            if char_ == '0': return 0 #invalid

            if start in memo: return memo[start] #MEMOIZATION
            
            #here:
            #case 1: we decode just the start character as single letter
            #case 2: we decode start and start +1 as letter -> CONSTRAINTS must be <= 26
            if start + 1 >= len(s): #start is last character, just decode that single digit
                counter = recursion(start+1)
            else:
                next = s[start +1]
                #1 term: just decode start as letter
                #2 term: decode (start & start+1) as letter
                #so at max we have +2 new valid decoding ways -> constraint
                if 10 <= int(char_+next) <= 26:
                    counter = recursion(start +1) + recursion(start+2)
                else:
                    #fallback to decoding just start
                    counter = recursion(start +1)

            #save counter to memo
            memo[start] = counter

            return counter
        
        return recursion(0)

        

        