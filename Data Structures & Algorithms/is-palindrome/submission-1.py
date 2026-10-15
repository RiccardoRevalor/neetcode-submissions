class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <=1 : return True
        #init 2 pointers
        l = 0
        r = n-1
        s = s.lower()


        while l <= r:
            #edge cases, not alèhanumeric, or numbers
            if not s[l].isalnum(): 
                l+=1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            if not s[l] == s[r]: return False

            l+=1
            r -=1

        return True

        