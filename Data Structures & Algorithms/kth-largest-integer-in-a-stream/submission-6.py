class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #solution with minHeap
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        #the min heap needs to have size k, since we do not remove elements, so we already discard the len(nums) -k elements that we do not need
        #if theb minHeap has a size > k already, if not pass
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        #add val and return kth largest
        #kth largest = element 0 from minHeap of size k
        heapq.heappush(self.minHeap, val)
        #if now the len of minHeap is > k, we pop 1 element, the (k-1) largest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        #kth largest, is the smallest element in the minHeap, aka element 0
        return self.minHeap[0]
        
