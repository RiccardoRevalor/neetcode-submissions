class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.acc = {}
        for n in nums:
            if not n in self.acc: self.acc[n] = 1
            else: self.acc[n] += 1

        descending = dict(sorted(self.acc.items(), key= lambda pair: pair[1],    reverse=True))

        #print(descending.keys())

        topK = list(descending.keys())[:k]

        return topK

        

        