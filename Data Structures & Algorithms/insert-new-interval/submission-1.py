class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            interval_i = intervals[i]
            #if interval_i has an end value < newInterval: append it to output
            if interval_i[1] < newInterval[0]:
                res.append(interval_i)
            else: break

        #case 1: we have appended all interval already -> it means newInterval must go at the end
        if len(res) == len(intervals):
            res.append(newInterval)
            return res

        #case 2: i is an interval whiose start value is > than new Interval'e end value
        #in this case we do: res + [newInterval] + [higher intervals]
        stopInterval = intervals[i]
        if stopInterval[0] > newInterval[1]:
            res.append(newInterval)
            while i < len(intervals):
                res.append(intervals[i])
                i+=1
            return res


        #case 3: overlapping interval with newInterval
        #in this case i have to fuze stopInterval with newInterval
        newnewInterval = [min(stopInterval[0], newInterval[0]), max(newInterval[1], stopInterval[1])] #[1,5]
        #now check that this new interval does not overlap with interval at i+1
        #if it does, we have to ufze that interval as well
        j = i+1
        while j < len(intervals):
            nextInterval = intervals[j]
            #[4,6]
            if nextInterval[0] <= newnewInterval[1]:
                newnewInterval = [min(nextInterval[0], newnewInterval[0]), max(newnewInterval[1], nextInterval[1])]
            
            else: break

            j+=1

        #now we can insert the fuzed newnewinterval
        res.append(newnewInterval)

        #now add all others till end
        while j < len(intervals):
            res.append(intervals[j])
            j+=1

        return res





            
        