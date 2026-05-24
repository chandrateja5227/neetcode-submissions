class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        list = []
        sublist = []
        def dfs(index):
            if index >= len(nums):
                list.append(sublist.copy())
                return

            sublist.append(nums[index])
            dfs(index+1)
            sublist.pop()
            dfs(index+1)

            return
        dfs(0)
        return list

        



        
        