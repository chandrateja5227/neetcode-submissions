class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0 
        right = len(nums)-1
        index = 0
        mid = 0
        while left <= right:
            mid = (left + right) // 2
            index = mid
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:     
                index = mid + 1           
                left = mid + 1
            else:
                index = mid
                right = mid - 1             
                
        return index
        


        
        