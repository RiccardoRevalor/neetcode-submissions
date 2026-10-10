class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums, reverse=True)
        self.k = k
        

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.arr) and self.arr[i] >= val:
            i +=1
        self.arr.insert(i, val)

        return self.arr[self.k -1]
        
