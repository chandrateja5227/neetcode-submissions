class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        output = [0]*len(nums)
        for i in range(len(nums)):
            if i:
                prefix[i] = nums[i] * prefix[i-1]
            else:
                prefix[i] = nums[i]


        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i] * suffix[i+1]

        for i in range(len(nums)):
            if i == 0:
                output[i] = suffix[i+1]
            elif i == len(nums) - 1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * suffix[i+1]

        return output

        