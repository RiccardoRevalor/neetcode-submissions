class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.compl = {}
        for i, n in enumerate(nums):
            com = target - n
            if com in self.compl: 
                return [self.compl[com], i]
            else: self.compl[n] = i
        return [None]
        