class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        start = goal -1 #startin gindex

        #can start reach the goal?

        while start >= 0:
            if start + nums[start] >= goal:
                #i can reach goal from start
                #now goal becomes
                goal = start
                start -=1
            else:
                #keep goal fixes, move start
                start -=1

        return goal == 0
        