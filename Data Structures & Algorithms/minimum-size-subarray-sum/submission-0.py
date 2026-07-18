class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        left = 0
        right = 0
        sum = 0
        result = [left , right ,sum] 
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                if result and result[2]:
                    if (right - left + 1) <  (result[1] - result[0] + 1):
                        result = [left , right ,sum] 
                else:
                    result = [left, right,sum]
                sum-=nums[left]
                left+=1
            right+=1
        
        return result[1] - result[0] + 1 if result[2] >= target else 0