import math

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        s_piles = sorted(piles)
        left = 1
        right = s_piles[len(s_piles)-1]
        min_k = right
        while left <=right:
            mid = (left + right)//2
            
            hours=0
            for i in range(len(s_piles)):
                hours+= math.ceil(s_piles[i]/mid)
                
            if hours<=h:
                min_k = min(min_k,mid)
                right = mid-1
            else:
                left = mid+1

        return min_k