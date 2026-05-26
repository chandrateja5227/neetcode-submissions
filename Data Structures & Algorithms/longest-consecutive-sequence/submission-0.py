class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        starts = []
        res = 1
        hashset = set(nums)

        for i in nums:
            if i-1 not in hashset:
                starts.append(i)
        
        count = 1
        start = 0
     
        while start < len(starts):
            if starts[start] + count in hashset:
                count+=1 
            else:
                start += 1
                res = max(res,count)
                count = 1
        return res

        