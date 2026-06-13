class Solution:
    def findMin(self, nums: List[int]) -> int:

        minN = nums[0]

        left = 0
        right = len(nums)-1

        while(left <= right):
            minN = min(minN, nums[left], nums[right])
            if nums[left] < nums[right]:
                return minN
            else:
                mid = (right + left) // 2
                minN = min(minN, nums[mid])
                if nums[left] <= nums[mid]:
                    left = mid+1
                else:
                    right = mid-1

        return minN