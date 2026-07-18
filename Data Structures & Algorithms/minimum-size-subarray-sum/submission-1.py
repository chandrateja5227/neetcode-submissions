class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        left = 0
        right = 0
        sum = 0
        result = float('inf') 
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                result = min(result , (right - left + 1))
                sum-=nums[left]
                left+=1
            right+=1
        
        return result if result != float('inf') else 0