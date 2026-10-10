class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #solution with quickselect, the best one
        #convert it to corresponding index in sorted order
        k = len(nums) -k
        
        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                #if number is higher than pivot, skip it, it will be partitioned to the right


            #at the end the p is at the last element of the (< pivot) set
            #so swap the pivot with nums[p]
            #so we have : (< pivot set) pivot (> pivot set)
            nums[p], nums[r] = pivot, nums[p]

            #now compare p with k
            if p > k: 
                #continue quickselect on left set
                return quickSelect(l, p-1)
            elif p < k:
                #continue quicselect on right part
                return quickSelect(p+1, r)
            else:
                #p==k -> found kth largest el
                return nums[p]

        return quickSelect(0, len(nums)-1)




        