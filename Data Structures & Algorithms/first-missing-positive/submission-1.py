
from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        hashmap = Counter(nums)
        print(hashmap)
        minNum = len(nums) + 1
        for i in range(1,len(nums)+1):
            print(hashmap.get(i , 0))
            if hashmap.get(i , 0) == 0:              
                minNum = i
                break

        return minNum


            

        