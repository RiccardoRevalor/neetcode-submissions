class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #better solution: use heap
        #min heap
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]