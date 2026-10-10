class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sHeap = [-s for s in stones] #in python we DO NOT have maxHeap

        heapq.heapify(sHeap)

        while (len(sHeap)) > 1:
            #pop 2 largest stones
            large0 = heapq.heappop(sHeap)
            large1 = heapq.heappop(sHeap)

            if large0 == large1: continue #both destroyed
            #case: large0 > large1
            heapq.heappush(sHeap, large0 - large1)

        #if heap is empty: 0, otherwise weights of last stone
        heapq.heappush(sHeap, 0)
        return sHeap[0] * (-1)

        