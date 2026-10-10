class MedianFinder:

    def __init__(self):
        #naive: create array, then sort it and find median
        #better: use heaps
        self.large = [] #largest, it has to be a min heap
        self.small = [] #smallest, it has to be a max heap
        #if stream is even: median = (max + min)/2
        #if stream is odd: median = max element of larger heap
        #how can i balance heaps?

        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)

        else:
            heapq.heappush(self.small, num * (-1)) #cause in python maxheaps do not exist
        
        #now try to mantain thme balanced, at mopst by 1 difference
        if len(self.small) > 1 + len(self.large):
            #unbalanced
            #take from small, add in large
            #take max from small
            maxsmall = (-1) * heapq.heappop(self.small)
            heapq.heappush(self.large, maxsmall)
        
        if len(self.large) > 1 + len(self.small):
            #find min from large, add it to small
            minlarge = heapq.heappop(self.large)
            heapq.heappush(self.small, minlarge * (-1))

        
        

    def findMedian(self) -> float:
        #2 cases
        #1: len of the heaps is same-> take min of large and max of min for median
        #2: len of one hip is higher:
        #take either the max of small, or min of large, that is the median
        if len(self.small) == len(self.large):
            return 0.5 * ((-1)*self.small[0] + self.large[0])

        if  len(self.small) == 1 + len(self.large):
            return -1 * self.small[0]
        
        #else, return min of large
        return self.large[0]
        
        