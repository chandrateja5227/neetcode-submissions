class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        stack  = []
        result = [0] * len(temperatures)

        for index in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                prev = stack.pop()
                result[prev] = (index - prev) 

            stack.append(index)

        return result