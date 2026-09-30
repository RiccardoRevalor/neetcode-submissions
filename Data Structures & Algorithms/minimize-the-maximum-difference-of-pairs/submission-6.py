class Solution:

    
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums_sorted = sorted(nums)
        low = 0
        high = nums_sorted[-1] - nums_sorted[0]

        def check(limit):
            count = 0 #need to be p to return true
            index = 0
            while index < len(nums) - 1:
                n0 = nums_sorted[index]
                n1 = nums_sorted[index+1]
                if abs(n1-n0) <= limit:
                    index +=2
                    count +=1
                else:
                    index += 1
            return count >= p


        while low < high:
            mid = (low + high) // 2
            if check(mid):
                high = mid
            else: low = mid + 1

        return low

        