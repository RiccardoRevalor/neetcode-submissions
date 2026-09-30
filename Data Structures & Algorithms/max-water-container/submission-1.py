class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxW = -1
        n = len(heights)
        i = 0
        j = n-1

        while i < j:
            h_i = heights[i]
            h_j = heights[j]
            area_height = min(h_i, h_j)
            area_width = j-i
            area = area_height * area_width
            if area > maxW: 
                maxW = area
            
            if heights[i] < heights[j]:
                i +=1
            else:
                j -= 1
        
        return maxW


        