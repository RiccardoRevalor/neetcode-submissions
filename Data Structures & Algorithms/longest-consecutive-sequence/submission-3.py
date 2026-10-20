class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #use hash set again but the trick is: only numbers taht does not have num-1 in set are actually sequence starters!
        l = 0
        store = set(nums)

        for num in nums:
            if not num-1 in store:
                #nums can start a new seq
                l_i = 0
                curr = num

                while curr in store:
                    curr+=1
                    l_i+=1
                
                l = max(l_i, l)
        
        return l

        