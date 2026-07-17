class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

       

        left = 0
        right = 0
        result = [0, k - 1]
        while right < len(arr):
            if (right - left + 1) > k:
                if abs(arr[right] - x) < abs(arr[left] - x):
                    left += 1
                    result = [left, right]
                else:
                    left+=1
            else:
                result[1] = right        
            right+=1


        return arr[result[0]:result[1]+1]