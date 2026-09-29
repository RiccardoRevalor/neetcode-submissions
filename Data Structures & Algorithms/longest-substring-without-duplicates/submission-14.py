class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0
        
        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[left])
                left +=1 #this is teh start of the enw substring
            
            seen.add(ch) #the duplicate/ch at index 0 is the 1st character of new substring

            longest = max(longest, right -left +1)
        
        return longest
            
            
            
            
            
            
            
    
                
        

            




        