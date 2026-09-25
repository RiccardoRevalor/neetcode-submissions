class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.occ = {}
        for n in nums:
            if n in self.occ: return True
            self.occ[n] = 1
        return False
        