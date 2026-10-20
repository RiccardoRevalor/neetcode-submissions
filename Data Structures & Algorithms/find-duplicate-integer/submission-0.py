class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #naive solution: use hashmap
        dup = {}

        for n in nums:
            if n in dup.keys(): return n
            else: dup[n] = 1

        
        