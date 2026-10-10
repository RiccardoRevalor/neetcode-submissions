class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #maxHeap
        heap = []
        for p in points:
            d = math.sqrt(p[0]**2 + p[1]**2) * (-1) #since python does not have maxHeaps
            #so I'm gonna use a minHeap with negative distances
            heapq.heappush(heap, (d, p)) #(key: distance_neg, value: point)
            if len(heap) > k:
                #pop farthest point
                heapq.heappop(heap)
        
        res = [p[1] for p in heap]
        return res



        