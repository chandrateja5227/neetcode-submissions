class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        

        maxA = 0
        stack = []
        bar = 0
        start = 0
        for bar in range(len(heights)):
            start = bar
            while stack and stack[-1][0] > heights[bar]:
                h , index = stack.pop()
                start = index
                maxA = max(maxA , h * (bar-index))

            stack.append((heights[bar] , start))

        for h, index in stack:
            maxA = max(maxA, h * (len(heights) - index))

        return maxA