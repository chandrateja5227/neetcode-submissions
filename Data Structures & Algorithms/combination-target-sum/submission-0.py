class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

       
        lst = []
        sublist = []

        def dfs(sum, start_index):
            if sum == target:
                lst.append(sublist.copy())
                return
            if sum > target:
                return

            for i in range(start_index, len(nums)):
                val = nums[i]
                sum += val
                sublist.append(val)
                dfs(sum, i)
                temp = sublist.pop()
                sum -= temp

            return
        dfs(0, 0)
        return lst