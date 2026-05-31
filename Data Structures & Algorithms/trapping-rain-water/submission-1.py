class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        maxleft = height[0]
        maxright = height[len(height)-1]
        left = 0
        right = len(height)-1
        result = 0
        while left < right:
            if maxleft < maxright:
                left+=1
                maxleft = max(maxleft , height[left])
                result += maxleft - height[left]

            else:
                right-=1
                maxright = max(maxright,height[right])
                result += maxright - height[right]

        return result
           



    


        