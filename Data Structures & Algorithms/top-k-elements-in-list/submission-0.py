from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)
        group = [[] for _ in range(len(nums) + 1)]
        for key, value in freq.items():
            group[value].append(key)
        
        res = []
        for i in range(len(group) - 1, 0, -1):
            for num in group[i]:
                res.append(num)
                if len(res) == k:
                    return res