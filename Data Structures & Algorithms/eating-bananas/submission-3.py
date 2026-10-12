class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #sol with binary search
        #upper bound is k = max(piles)
        #brute force
        #try with all combinations from 1 to k
        k_upperBound = max(piles)
        l = 1
        r = k_upperBound
        best_k = k_upperBound

        while l <= r:
            k_try = (l+r) // 2
            #try with the km
            h_m = h
            for p in piles:
                h_m -= math.ceil(p / k_try)
                if h_m < 0: break
            
            
            if h_m >= 0:
                #we can finish in time
                #so record k and try to finishes slower and record a lower k
                #so look at left part
                best_k = k_try
                r = k_try-1
            elif h_m < 0:
                #we are too slow!
                #look at the right part
                l = k_try+1

        return best_k
