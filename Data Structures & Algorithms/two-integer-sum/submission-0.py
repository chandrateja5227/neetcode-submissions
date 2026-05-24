class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i in range(len(nums)):
            for j in range(i+1 ,len(nums)):
               
                if i == j:
                    continue
                map[nums[i] + nums[j]] = [i,j]


        return map[target]
        