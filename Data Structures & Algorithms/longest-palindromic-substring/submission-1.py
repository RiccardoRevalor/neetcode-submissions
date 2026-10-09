class Solution:
    def longestPalindrome(self, s: str) -> str:
        def checkPal(left, right):
            #in the odd case, left and right are the same sttarting index:
            #aba -> left = right = b
            #here we also have the subcase of 1 single word
            #in even case, left and right are two adjacent indexes: 2002 ->
            #left = 0, right = the other 0
            n = len(s)
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            #pal found starts from left +1 and goes all way up to right -1
            return left+1, right -1

        

        #now, i have to take the longest pal
        res = None
        resLen = -1

        for i in range(len(s)):
            #try to check if i is the center of a pal with odd lenght
            l_odd, r_odd = checkPal(i,i)
            #try to check if i is the center of a pal with even lenght
            l_even, r_even = checkPal(i, i+1)

            len_odd = r_odd - l_odd +1
            len_even = r_even - l_even +1
            maxI = max(len_odd, len_even)
            if maxI > resLen:
                resLen = maxI
                if maxI == len_odd:
                    res = l_odd
                else:
                    res = l_even

        return s[res:res+resLen]
        
        