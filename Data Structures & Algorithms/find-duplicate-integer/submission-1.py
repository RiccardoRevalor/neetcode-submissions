class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #solution using Floyd's algorithm

        slow, fast = 0,0

        while True:
            #break as soon as slow and fastland on same index
            slow = nums[slow] #1 jump of slow, 1 index at a time
            fast = nums[nums[fast]] #1 jump of fast: 2 indices at a time

            if slow == fast: break

        #now set another slow point at beginning
        slow2 = 0

        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        return slow