class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water = 0;

        i = 0
        j = len(heights)-1

        while i < j:
            distance = j-i
            if heights[i] <= heights[j]:
                max_water = max(max_water, distance*heights[i])
                i+=1
            else:
                max_water = max(max_water, distance*heights[j])
                j-=1
        
        return max_water
            


        