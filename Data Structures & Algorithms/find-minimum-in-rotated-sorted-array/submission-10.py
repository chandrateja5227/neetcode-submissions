class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        result = nums[left]

        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                 result = min(nums[left] , result)
                 left = mid + 1
            else:
                if nums[mid+ 1] <= nums[right]:
                    result = min(result , nums[mid])
                    right = mid - 1
                else:
                    result = min(result , nums[mid])
                    left = mid + 1

        return result
        