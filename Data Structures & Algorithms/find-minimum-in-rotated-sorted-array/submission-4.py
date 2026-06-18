class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0

        right = len(nums)-1

        min_num = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                return min(min_num ,nums[left])

            mid = (left+ right) // 2
            min_num = min(min_num ,nums[mid])
            if nums[mid] > nums[right]:                
                left = mid+1
            else:
                right = mid-1

        return min_num
        
