class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #naive/bruteforce sol, works but exceed time limit cause it is O(n^2)
        """
        best = heights[0]
        n = len(heights)

        for h in range(n):
            i = h
            #extend to right and see how fare you can go by mantaining the height
            while i < n and heights[i] >= heights[h]:
                i +=1

            j = h
            #extend to left and se how fare you can go
            while j >= 0 and heights[j] >= heights[h]:
                j -= 1

            #max area is (i-j)*h
            best = max(best, (i-j-1)*heights[h])

        return best
        """

        #stack
        #the bottleneck in my solution is: i need to go back to find te index of nearest shorter bar than heights[h], and do so for the right as well

        #find closer height < current on left side
        n = len(heights)
        shorterLeft = [-1] * n 
        stack = []

        for i in range(n):
            #iterate throught heights, put closer shorter left in stack
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() #higher bars, do noit want them

            if stack: shorterLeft[i] = stack[-1] #top of stack is closer lesser left height index
            stack.append(i)

        #do the same to record on another stack the index of closer shorter right bar, for each bar

        #find closer height < current on right side
        shorterRight = [n] * n 
        stack = []

        for i in range(n-1, -1, -1):
            #iterate throught heights, put closer shorter left in stack
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() #higher bars, do noit want them

            if stack: shorterRight[i] = stack[-1] #top of stack is closer lesser left height index than number on index i
            stack.append(i)


        #now like my bruteforce, i iterate on bars, but this time in already have precomputed the closest index of shortest bars

        best = heights[0]

        for h in range(n):

            #max area is (closershorter on right - closer shortest on left-1)*h
            best = max(best, (shorterRight[h] - shorterLeft[h]-1)*heights[h])

        return best




            

        



            



        


        